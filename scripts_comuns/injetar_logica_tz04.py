import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-04-aqd"
    
    ips = {
        "tz_aqd_001_adc": {
            "ch": "1F",
            "ports": "adc_in : in std_logic_vector(11 downto 0)",
            "signals": "",
            "reset": "",
            "core": "int_data(11 downto 0) <= adc_in;",
            "tb_sigs": "signal adc_in : std_logic_vector(11 downto 0) := (others => '0');",
            "tb_map": "adc_in => adc_in,",
            "tb_stim": "adc_in <= x\"123\"; wait for 50 ns; adc_in <= x\"ABC\"; wait for 50 ns;"
        },
        "tz_aqd_002_dac": {
            "ch": "20",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        dac_out : out std_logic_vector(11 downto 0)",
            "signals": "",
            "reset": "dac_out <= (others => '0');",
            "core": "dac_out <= din(11 downto 0);\n        int_data(11 downto 0) <= din(11 downto 0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal dac_out : std_logic_vector(11 downto 0);",
            "tb_map": "din => din, dac_out => dac_out,",
            "tb_stim": "din <= x\"0000_0555\"; wait for 50 ns;"
        },
        "tz_aqd_003_dig_sensor": {
            "ch": "21",
            "ports": "sensor_in : in std_logic",
            "signals": "signal s_d : std_logic;",
            "reset": "s_d <= '0';",
            "core": "s_d <= sensor_in; int_data(0) <= s_d;",
            "tb_sigs": "signal sensor_in : std_logic := '0';",
            "tb_map": "sensor_in => sensor_in,",
            "tb_stim": "sensor_in <= '1'; wait for 30 ns; sensor_in <= '0'; wait for 30 ns;"
        },
        "tz_aqd_004_ana_acq": {
            "ch": "22",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        start_conv : out std_logic;\n        adc_data : in std_logic_vector(15 downto 0)",
            "signals": "signal active : std_logic;",
            "reset": "start_conv <= '0'; active <= '0';",
            "core": "if din(0) = '1' then active <= '1'; start_conv <= '1'; else active <= '0'; start_conv <= '0'; end if;\n        int_data(15 downto 0) <= adc_data;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal start_conv : std_logic;\n    signal adc_data : std_logic_vector(15 downto 0) := x\"0000\";",
            "tb_map": "din => din, start_conv => start_conv, adc_data => adc_data,",
            "tb_stim": "din(0) <= '1'; adc_data <= x\"1234\"; wait for 20 ns; din(0) <= '0'; wait for 20 ns;"
        },
        "tz_aqd_005_pulse_cap": {
            "ch": "23",
            "ports": "pulse_in : in std_logic",
            "signals": "signal p_d : std_logic;\n    signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "p_d <= '0'; counter <= (others => '0');",
            "core": "p_d <= pulse_in;\n        if pulse_in = '1' then counter <= counter + 1;\n        elsif p_d = '1' and pulse_in = '0' then int_data <= std_logic_vector(counter); counter <= (others => '0'); end if;",
            "tb_sigs": "signal pulse_in : std_logic := '0';",
            "tb_map": "pulse_in => pulse_in,",
            "tb_stim": "pulse_in <= '1'; wait for 100 ns; pulse_in <= '0'; wait for 50 ns;"
        },
        "tz_aqd_006_freq_meter": {
            "ch": "24",
            "ports": "sig_in : in std_logic",
            "signals": "signal p_d : std_logic;\n    signal edges : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);\n    signal time_base : unsigned(31 downto 0);",
            "reset": "p_d <= '0'; edges <= (others => '0'); time_base <= (others => '0');",
            "core": "p_d <= sig_in;\n        time_base <= time_base + 1;\n        if sig_in = '1' and p_d = '0' then edges <= edges + 1; end if;\n        if time_base = x\"05F5E100\" then int_data <= std_logic_vector(edges); edges <= (others => '0'); time_base <= (others => '0'); end if;",
            "tb_sigs": "signal sig_in : std_logic := '0';",
            "tb_map": "sig_in => sig_in,",
            "tb_stim": "sig_in <= '1'; wait for 10 ns; sig_in <= '0'; wait for 10 ns;"
        },
        "tz_aqd_007_per_meter": {
            "ch": "25",
            "ports": "sig_in : in std_logic",
            "signals": "signal p_d : std_logic;\n    signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "p_d <= '0'; counter <= (others => '0');",
            "core": "p_d <= sig_in;\n        if sig_in = '1' and p_d = '0' then int_data <= std_logic_vector(counter); counter <= (others => '0');\n        else counter <= counter + 1; end if;",
            "tb_sigs": "signal sig_in : std_logic := '0';",
            "tb_map": "sig_in => sig_in,",
            "tb_stim": "sig_in <= '1'; wait for 20 ns; sig_in <= '0'; wait for 100 ns; sig_in <= '1'; wait for 20 ns; sig_in <= '0';"
        },
        "tz_aqd_008_duty_meter": {
            "ch": "26",
            "ports": "sig_in : in std_logic",
            "signals": "signal high_cnt, total_cnt : unsigned(15 downto 0);\n    signal p_d : std_logic;",
            "reset": "high_cnt <= (others => '0'); total_cnt <= (others => '0'); p_d <= '0';",
            "core": "p_d <= sig_in;\n        total_cnt <= total_cnt + 1;\n        if sig_in = '1' then high_cnt <= high_cnt + 1; end if;\n        if sig_in = '1' and p_d = '0' then\n            int_data(31 downto 16) <= std_logic_vector(total_cnt);\n            int_data(15 downto 0) <= std_logic_vector(high_cnt);\n            total_cnt <= (others => '0'); high_cnt <= (others => '0');\n        end if;",
            "tb_sigs": "signal sig_in : std_logic := '0';",
            "tb_map": "sig_in => sig_in,",
            "tb_stim": "sig_in <= '1'; wait for 30 ns; sig_in <= '0'; wait for 70 ns; sig_in <= '1'; wait for 20 ns;"
        },
        "tz_aqd_009_multi_acq": {
            "ch": "27",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        ch_sel : out std_logic_vector(2 downto 0);\n        adc_in : in std_logic_vector(11 downto 0)",
            "signals": "",
            "reset": "ch_sel <= \"000\";",
            "core": "ch_sel <= din(2 downto 0);\n        int_data(11 downto 0) <= adc_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal ch_sel : std_logic_vector(2 downto 0);\n    signal adc_in : std_logic_vector(11 downto 0) := x\"000\";",
            "tb_map": "din => din, ch_sel => ch_sel, adc_in => adc_in,",
            "tb_stim": "din(2 downto 0) <= \"011\"; adc_in <= x\"FFF\"; wait for 40 ns;"
        },
        "tz_aqd_010_timestamp": {
            "ch": "28",
            "ports": "event_in : in std_logic",
            "signals": "signal time_reg : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);\n    signal e_d : std_logic;",
            "reset": "time_reg <= (others => '0'); e_d <= '0';",
            "core": "time_reg <= time_reg + 1;\n        e_d <= event_in;\n        if event_in = '1' and e_d = '0' then int_data <= std_logic_vector(time_reg); end if;",
            "tb_sigs": "signal event_in : std_logic := '0';",
            "tb_map": "event_in => event_in,",
            "tb_stim": "wait for 200 ns; event_in <= '1'; wait for 10 ns; event_in <= '0';"
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

    print("Iniciando Injeção Blindada na Família TZ-04-AQD...")
    
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
            
        print(f" -> Lógica de Aquisição injetada em: {ip}")
        
    print("Injeção da Família 04 (Aquisição) concluída!")

if __name__ == "__main__":
    main()