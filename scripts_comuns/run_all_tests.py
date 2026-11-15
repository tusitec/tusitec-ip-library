import os
import subprocess

def run_cmd(cmd, cwd=None):
    cmd_str = " ".join(cmd)
    wsl_cmd = ["wsl", "bash", "-c", f"cd /mnt/f/projetos/tusitec-ip-library && {cmd_str}"]
    result = subprocess.run(wsl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0, result.stdout + result.stderr

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        for f in files:
            if f.lower() == filename.lower():
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, start=r"F:\projetos\tusitec-ip-library")
                return rel_path.replace("\\", "/")
    return None

def main():
    base_dir = r"F:\projetos\tusitec-ip-library"
    log_file = os.path.join(base_dir, "scripts_comuns", "relatorio_falhas.log")
    
    print("Iniciando Bateria de Testes Sistemicos - Tusitec IP Library")
    print("-" * 65)
    
    pkg_rel_path = find_file("tusitec_tlink_pkg.vhd", os.path.join(base_dir, "tz-00-hub"))
    if not pkg_rel_path: return
        
    success, log = run_cmd(["ghdl", "-a", pkg_rel_path], cwd=base_dir)
    if not success: return

    hub_rel_path = find_file("operador_meec_hub.vhd", os.path.join(base_dir, "tz-00-hub"))
    if hub_rel_path: run_cmd(["ghdl", "-a", hub_rel_path], cwd=base_dir)

    pass_count = 0
    falhas_rastreadas = []
    
    for family in sorted(os.listdir(base_dir)):
        if not family.startswith("tz-") or family == "tz-00-hub": continue
        family_path = os.path.join(base_dir, family)
        if not os.path.isdir(family_path): continue
            
        for ip_core in sorted(os.listdir(family_path)):
            ip_path = os.path.join(family_path, ip_core)
            if not os.path.isdir(ip_path): continue
                
            rtl_file = find_file(f"{ip_core}.vhd", ip_path)
            tb_name = f"tb_{ip_core}"
            tb_file = find_file(f"{tb_name}.vhd", ip_path)
            
            if not (rtl_file and tb_file): continue
            
            # A. Sintaxe RTL
            success_rtl, _ = run_cmd(["ghdl", "-a", rtl_file], cwd=base_dir)
            if not success_rtl:
                print(f"[FAIL] {ip_core:<28} -> Erro de Sintaxe RTL")
                falhas_rastreadas.append((ip_core, "Erro de Sintaxe RTL"))
                continue
                
            # B. Sintaxe Testbench
            success_tb, _ = run_cmd(["ghdl", "-a", tb_file], cwd=base_dir)
            if not success_tb:
                print(f"[FAIL] {ip_core:<28} -> Erro de Sintaxe no Testbench")
                falhas_rastreadas.append((ip_core, "Erro de Sintaxe no Testbench"))
                continue
                
            # C. Simulacao Dinamica
            run_cmd(["ghdl", "-e", tb_name], cwd=base_dir)
            success_run, _ = run_cmd(["ghdl", "-r", tb_name, "--stop-time=500ns"], cwd=base_dir)
            
            if success_run:
                print(f"[PASS] {ip_core:<28} -> T-Link Sincronizado")
                pass_count += 1
            else:
                print(f"[FAIL] {ip_core:<28} -> Falha na Simulacao Temporal")
                falhas_rastreadas.append((ip_core, "Falha na Simulacao Temporal (Maquina de Estados quebrou)"))
                
    print("-" * 65)
    print(f"Resumo da Bateria: {pass_count} PASS | {len(falhas_rastreadas)} FAIL")
    
    with open(log_file, "w") as f:
        if not falhas_rastreadas:
            f.write("Sucesso absoluto. Nenhuma falha detectada.\n")
        else:
            f.write("RELATORIO DE QUARENTENA - IP CORES COM FALHA\n")
            f.write("=" * 65 + "\n")
            print("\n[ ALERTA ] Os seguintes IP Cores falharam e foram marcados:")
            for ip, motivo in falhas_rastreadas:
                linha = f"-> {ip:<25} : {motivo}"
                print(linha)
                f.write(linha + "\n")

if __name__ == "__main__":
    main()