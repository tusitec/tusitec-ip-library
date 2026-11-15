import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-08-sys"
    
    # Dicionário VHDL estrito para os 10 IPs de Sistemas e Interligação
    ips = {
        "tz_sys_001_softcore": {
            "ch": "47",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        instr_addr : out std_logic_vector(31 downto 0);\n        instr_data : in std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "instr_addr <= (others => '0');",
            "core": "instr_addr <= din;\n        int_data <= instr_data;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal instr_addr : std_logic_vector(31 downto 0);\n    signal instr_data : std_logic_vector(31 downto 0) := (others => '0');",
            "tb_map": "din => din, instr_addr => instr_addr, instr_data => instr_data,",
            "tb_stim": "din <= x\"00000004\"; instr_data <= x\"DEADBEEF\"; wait for 50 ns;"
        },
        "tz_sys_002_riscv": {
            "ch": "48",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        pc_out : out std_logic_vector(31 downto 0);\n        ir_in : in std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "pc_out <= (others => '0');",
            "core": "pc_out <= din;\n        int_data <= ir_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal pc_out : std_logic_vector(31 downto 0);\n    signal ir_in : std_logic_vector(31 downto 0) := (others => '0');",
            "tb_map": "din => din, pc_out => pc_out, ir_in => ir_in,",
            "tb_stim": "din <= x\"00000008\"; ir_in <= x\"13370000\"; wait for 50 ns;"
        },
        "tz_sys_003_int_ctrl": {
            "ch": "49",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        irq_lines : in std_logic_vector(7 downto 0);\n        irq_req : out std_logic",
            "signals": "",
            "reset": "irq_req <= '0';",
            "core": "if irq_lines /= \"00000000\" and (irq_lines and din(7 downto 0)) /= \"00000000\" then irq_req <= '1'; else irq_req <= '0'; end if;\n        int_data(7 downto 0) <= irq_lines;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal irq_lines : std_logic_vector(7 downto 0) := (others => '0');\n    signal irq_req : std_logic;",
            "tb_map": "din => din, irq_lines => irq_lines, irq_req => irq_req,",
            "tb_stim": "din(7 downto 0) <= x\"FF\"; irq_lines <= x\"01\"; wait for 50 ns;"
        },
        "tz_sys_004_int_bus": {
            "ch": "4A",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        req_a : in std_logic;\n        req_b : in std_logic;\n        gnt_a : out std_logic;\n        gnt_b : out std_logic",
            "signals": "",
            "reset": "gnt_a <= '0'; gnt_b <= '0';",
            "core": "if req_a = '1' then gnt_a <= '1'; gnt_b <= '0'; elsif req_b = '1' then gnt_a <= '0'; gnt_b <= '1'; else gnt_a <= '0'; gnt_b <= '0'; end if;\n        int_data(0) <= req_a; int_data(1) <= req_b;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal req_a, req_b : std_logic := '0';\n    signal gnt_a, gnt_b : std_logic;",
            "tb_map": "din => din, req_a => req_a, req_b => req_b, gnt_a => gnt_a, gnt_b => gnt_b,",
            "tb_stim": "req_a <= '1'; wait for 20 ns; req_a <= '0'; req_b <= '1'; wait for 20 ns;"
        },
        "tz_sys_005_axi4_lite": {
            "ch": "4B",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        awaddr : out std_logic_vector(31 downto 0);\n        awvalid : out std_logic;\n        wdata : out std_logic_vector(31 downto 0);\n        wvalid : out std_logic",
            "signals": "",
            "reset": "awaddr <= (others => '0'); awvalid <= '0'; wdata <= (others => '0'); wvalid <= '0';",
            "core": "awaddr <= din; awvalid <= din(0); wdata <= din; wvalid <= din(0);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal awaddr, wdata : std_logic_vector(31 downto 0);\n    signal awvalid, wvalid : std_logic;",
            "tb_map": "din => din, awaddr => awaddr, awvalid => awvalid, wdata => wdata, wvalid => wvalid,",
            "tb_stim": "din <= x\"00000001\"; wait for 50 ns;"
        },
        "tz_sys_006_avalon": {
            "ch": "4C",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        address : out std_logic_vector(31 downto 0);\n        write_en : out std_logic;\n        writedata : out std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "address <= (others => '0'); write_en <= '0'; writedata <= (others => '0');",
            "core": "address <= din; write_en <= din(0); writedata <= din;\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal address, writedata : std_logic_vector(31 downto 0);\n    signal write_en : std_logic;",
            "tb_map": "din => din, address => address, write_en => write_en, writedata => writedata,",
            "tb_stim": "din <= x\"00000001\"; wait for 50 ns;"
        },
        "tz_sys_007_wishbone": {
            "ch": "4D",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        adr_o : out std_logic_vector(31 downto 0);\n        dat_o : out std_logic_vector(31 downto 0);\n        we_o : out std_logic;\n        stb_o : out std_logic",
            "signals": "",
            "reset": "adr_o <= (others => '0'); dat_o <= (others => '0'); we_o <= '0'; stb_o <= '0';",
            "core": "adr_o <= din; dat_o <= din; we_o <= din(0); stb_o <= din(0);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal adr_o, dat_o : std_logic_vector(31 downto 0);\n    signal we_o, stb_o : std_logic;",
            "tb_map": "din => din, adr_o => adr_o, dat_o => dat_o, we_o => we_o, stb_o => stb_o,",
            "tb_stim": "din <= x\"00000001\"; wait for 50 ns;"
        },
        "tz_sys_008_reg_bank": {
            "ch": "4E",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        reg_addr : in std_logic_vector(3 downto 0);\n        reg_rdata : out std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "reg_rdata <= (others => '0');",
            "core": "reg_rdata <= din;\n        int_data(3 downto 0) <= reg_addr;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal reg_addr : std_logic_vector(3 downto 0) := (others => '0');\n    signal reg_rdata : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, reg_addr => reg_addr, reg_rdata => reg_rdata,",
            "tb_stim": "din <= x\"12345678\"; reg_addr <= x\"A\"; wait for 50 ns;"
        },
        "tz_sys_009_soc_interconnect": {
            "ch": "4F",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        m0_req : in std_logic;\n        s0_ack : in std_logic;\n        m0_grant : out std_logic",
            "signals": "",
            "reset": "m0_grant <= '0';",
            "core": "m0_grant <= m0_req and s0_ack;\n        int_data(0) <= m0_req;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal m0_req, s0_ack : std_logic := '0';\n    signal m0_grant : std_logic;",
            "tb_map": "din => din, m0_req => m0_req, s0_ack => s0_ack, m0_grant => m0_grant,",
            "tb_stim": "m0_req <= '1'; s0_ack <= '1'; wait for 50 ns;"
        },
        "tz_sys_010_bus_bridge": {
            "ch": "50",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        ext_addr : out std_logic_vector(31 downto 0);\n        ext_data : out std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "ext_addr <= (others => '0'); ext_data <= (others => '0');",
            "core": "ext_addr <= din; ext_data <= din;\n        int_data <= din;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal ext_addr, ext_data : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, ext_addr => ext_addr, ext_data => ext_data,",
            "tb_stim": "din <= x\"A5A5A5A5\"; wait for 50 ns;"
        }
    }

    rtl_tpl = '''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity {ip} is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        {ports};
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of {ip} is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    {signals}
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            {reset}
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            {core}
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"{ch}";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
'''

    tb_tpl = '''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_{ip} is
end entity;

architecture sim of tb_{ip} is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    {tb_sigs}
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.{ip}
        port map (
            clk      => clk,
            rst_n    => rst_n,
            {tb_map}
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        {tb_stim}
        wait;
    end process;
end architecture sim;
'''

    print("A iniciar Injeção Blindada na Família TZ-08-SYS...")
    
    for ip, data in ips.items():
        ip_path = os.path.join(base_dir, ip)
        if not os.path.exists(ip_path): 
            continue
            
        rtl_dir = os.path.join(ip_path, "rtl")
        tb_dir = os.path.join(ip_path, "tb")
        os.makedirs(rtl_dir, exist_ok=True)
        os.makedirs(tb_dir, exist_ok=True)
            
        rtl_code = rtl_tpl.replace("{ip}", ip).replace("{ports}", data["ports"]).replace("{signals}", data["signals"]).replace("{reset}", data["reset"]).replace("{core}", data["core"]).replace("{ch}", data["ch"])
        with open(os.path.join(rtl_dir, f"{ip}.vhd"), "w", encoding="utf-8") as f:
            f.write(rtl_code)
            
        tb_code = tb_tpl.replace("{ip}", ip).replace("{tb_sigs}", data["tb_sigs"]).replace("{tb_map}", data["tb_map"]).replace("{tb_stim}", data["tb_stim"])
        with open(os.path.join(tb_dir, f"tb_{ip}.vhd"), "w", encoding="utf-8") as f:
            f.write(tb_code)
            
        print(f" -> Lógica de Sistemas injetada em: {ip}")
        
    print("Injeção da Família 08 (Sistemas) concluída!")

if __name__ == "__main__":
    main()