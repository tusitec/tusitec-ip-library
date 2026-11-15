import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-09-dbg"
    
    # Dicionário VHDL estrito para os 10 IPs de Debug e Teste
    ips = {
        "tz_dbg_001_logic_ana": {
            "ch": "51",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        probe_in : in std_logic_vector(15 downto 0);\n        trigger_match : out std_logic",
            "signals": "signal trig_val : std_logic_vector(15 downto 0);\n    signal match_reg : std_logic;",
            "reset": "trig_val <= (others => '0'); match_reg <= '0'; trigger_match <= '0';",
            "core": "trig_val <= din(15 downto 0);\n        if probe_in = trig_val then match_reg <= '1'; else match_reg <= '0'; end if;\n        trigger_match <= match_reg;\n        int_data(15 downto 0) <= probe_in;\n        int_data(16) <= match_reg;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal probe_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal trigger_match : std_logic;",
            "tb_map": "din => din, probe_in => probe_in, trigger_match => trigger_match,",
            "tb_stim": "din <= x\"0000_AAAA\"; wait for 20 ns; probe_in <= x\"AAAA\"; wait for 20 ns; probe_in <= x\"0000\"; wait for 20 ns;"
        },
        "tz_dbg_002_pat_gen": {
            "ch": "52",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        pat_out : out std_logic_vector(7 downto 0)",
            "signals": "signal cnt : unsigned(7 downto 0);\n    signal en : std_logic;",
            "reset": "cnt <= (others => '0'); en <= '0'; pat_out <= (others => '0');",
            "core": "en <= din(0);\n        if en = '1' then cnt <= cnt + 1; end if;\n        pat_out <= std_logic_vector(cnt);\n        int_data(7 downto 0) <= std_logic_vector(cnt);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal pat_out : std_logic_vector(7 downto 0);",
            "tb_map": "din => din, pat_out => pat_out,",
            "tb_stim": "din <= x\"0000_0001\"; wait for 100 ns; din <= x\"0000_0000\"; wait for 50 ns;"
        },
        "tz_dbg_003_test_sig": {
            "ch": "53",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        sig_out : out std_logic",
            "signals": "signal toggle : std_logic;",
            "reset": "toggle <= '0'; sig_out <= '0';",
            "core": "if din(0) = '1' then toggle <= not toggle; else toggle <= '0'; end if;\n        sig_out <= toggle;\n        int_data(0) <= toggle;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal sig_out : std_logic;",
            "tb_map": "din => din, sig_out => sig_out,",
            "tb_stim": "din <= x\"0000_0001\"; wait for 50 ns; din <= x\"0000_0000\"; wait for 50 ns;"
        },
        "tz_dbg_004_wave_cap": {
            "ch": "54",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        wave_in : in std_logic_vector(7 downto 0);\n        cap_done : out std_logic",
            "signals": "signal cnt : unsigned(7 downto 0);",
            "reset": "cnt <= (others => '0'); cap_done <= '0';",
            "core": "if din(0) = '1' then\n            if cnt < 255 then cnt <= cnt + 1; cap_done <= '0'; else cap_done <= '1'; end if;\n        else cnt <= (others => '0'); cap_done <= '0'; end if;\n        int_data(7 downto 0) <= wave_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal wave_in : std_logic_vector(7 downto 0) := (others => '0');\n    signal cap_done : std_logic;",
            "tb_map": "din => din, wave_in => wave_in, cap_done => cap_done,",
            "tb_stim": "din <= x\"0000_0001\"; wave_in <= x\"55\"; wait for 50 ns; din <= x\"0000_0000\"; wait for 20 ns;"
        },
        "tz_dbg_005_err_count": {
            "ch": "55",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        err_pulse : in std_logic;\n        err_total : out std_logic_vector(15 downto 0)",
            "signals": "signal e_d : std_logic;\n    signal cnt : unsigned(15 downto 0);",
            "reset": "e_d <= '0'; cnt <= (others => '0'); err_total <= (others => '0');",
            "core": "e_d <= err_pulse;\n        if din(0) = '1' then cnt <= (others => '0');\n        elsif err_pulse = '1' and e_d = '0' then cnt <= cnt + 1; end if;\n        err_total <= std_logic_vector(cnt);\n        int_data(15 downto 0) <= std_logic_vector(cnt);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal err_pulse : std_logic := '0';\n    signal err_total : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, err_pulse => err_pulse, err_total => err_total,",
            "tb_stim": "err_pulse <= '1'; wait for 20 ns; err_pulse <= '0'; wait for 20 ns; err_pulse <= '1'; wait for 20 ns; err_pulse <= '0'; wait for 20 ns; din <= x\"0000_0001\"; wait for 20 ns;"
        },
        "tz_dbg_006_crc": {
            "ch": "56",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        data_in : in std_logic_vector(7 downto 0);\n        crc_out : out std_logic_vector(15 downto 0)",
            "signals": "signal crc_reg : std_logic_vector(15 downto 0);",
            "reset": "crc_reg <= x\"FFFF\"; crc_out <= (others => '0');",
            "core": "if din(0) = '1' then crc_reg <= x\"FFFF\";\n        else crc_reg(15 downto 8) <= crc_reg(7 downto 0); crc_reg(7 downto 0) <= data_in; end if;\n        crc_out <= crc_reg;\n        int_data(15 downto 0) <= crc_reg;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal data_in : std_logic_vector(7 downto 0) := (others => '0');\n    signal crc_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, data_in => data_in, crc_out => crc_out,",
            "tb_stim": "data_in <= x\"AA\"; wait for 20 ns; data_in <= x\"BB\"; wait for 20 ns; din <= x\"0000_0001\"; wait for 20 ns;"
        },
        "tz_dbg_007_prbs": {
            "ch": "57",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        prbs_out : out std_logic_vector(7 downto 0)",
            "signals": "signal lfsr : std_logic_vector(7 downto 0);",
            "reset": "lfsr <= x\"FF\"; prbs_out <= (others => '0');",
            "core": "if din(0) = '1' then lfsr <= x\"FF\";\n        else lfsr <= lfsr(6 downto 0) & (lfsr(7) xor lfsr(5) xor lfsr(4) xor lfsr(3)); end if;\n        prbs_out <= lfsr;\n        int_data(7 downto 0) <= lfsr;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal prbs_out : std_logic_vector(7 downto 0);",
            "tb_map": "din => din, prbs_out => prbs_out,",
            "tb_stim": "wait for 100 ns; din <= x\"0000_0001\"; wait for 20 ns; din <= x\"0000_0000\"; wait for 50 ns;"
        },
        "tz_dbg_008_perf_mon": {
            "ch": "58",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        event_a : in std_logic;\n        event_b : in std_logic;\n        cycles : out std_logic_vector(31 downto 0)",
            "signals": "signal cnt : unsigned(31 downto 0);\n    signal active : std_logic;",
            "reset": "cnt <= (others => '0'); active <= '0'; cycles <= (others => '0');",
            "core": "if din(0) = '1' then cnt <= (others => '0'); active <= '0';\n        else\n            if event_a = '1' then active <= '1'; elsif event_b = '1' then active <= '0'; end if;\n            if active = '1' then cnt <= cnt + 1; end if;\n        end if;\n        cycles <= std_logic_vector(cnt);\n        int_data <= std_logic_vector(cnt);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal event_a, event_b : std_logic := '0';\n    signal cycles : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, event_a => event_a, event_b => event_b, cycles => cycles,",
            "tb_stim": "event_a <= '1'; wait for 10 ns; event_a <= '0'; wait for 50 ns; event_b <= '1'; wait for 10 ns; event_b <= '0'; wait for 30 ns;"
        },
        "tz_dbg_009_bus_mon": {
            "ch": "59",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        bus_valid : in std_logic;\n        bus_data : in std_logic_vector(31 downto 0);\n        err_flag : out std_logic",
            "signals": "signal e_reg : std_logic;",
            "reset": "e_reg <= '0'; err_flag <= '0';",
            "core": "if din(0) = '1' then e_reg <= '0';\n        elsif bus_valid = '1' and bus_data = x\"00000000\" then e_reg <= '1'; end if;\n        err_flag <= e_reg;\n        int_data(0) <= e_reg;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal bus_valid : std_logic := '0';\n    signal bus_data : std_logic_vector(31 downto 0) := (others => '0');\n    signal err_flag : std_logic;",
            "tb_map": "din => din, bus_valid => bus_valid, bus_data => bus_data, err_flag => err_flag,",
            "tb_stim": "bus_valid <= '1'; bus_data <= x\"12345678\"; wait for 20 ns; bus_data <= x\"00000000\"; wait for 20 ns; bus_valid <= '0'; wait for 20 ns;"
        },
        "tz_dbg_010_trigger": {
            "ch": "5A",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        trig_in : in std_logic;\n        trig_out : out std_logic",
            "signals": "signal t_reg : std_logic;",
            "reset": "t_reg <= '0'; trig_out <= '0';",
            "core": "if din(0) = '1' then t_reg <= '0';\n        elsif trig_in = '1' then t_reg <= '1'; end if;\n        trig_out <= t_reg;\n        int_data(0) <= t_reg;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal trig_in : std_logic := '0';\n    signal trig_out : std_logic;",
            "tb_map": "din => din, trig_in => trig_in, trig_out => trig_out,",
            "tb_stim": "trig_in <= '1'; wait for 10 ns; trig_in <= '0'; wait for 40 ns; din <= x\"0000_0001\"; wait for 20 ns;"
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

    print("A iniciar Injeção Blindada na Família TZ-09-DBG...")
    
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
            
        print(f" -> Lógica de Debug injetada em: {ip}")
        
    print("Injeção da Família 09 (Debug) concluída!")

if __name__ == "__main__":
    main()