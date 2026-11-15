import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-03-ctl"
    
    # Dicionário VHDL estrito para os 10 IPs de Controle
    ips = {
        "tz_ctl_001_pwm": {
            "ch": "15",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        pwm_out : out std_logic",
            "signals": "signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "pwm_out <= '0'; counter <= (others => '0');",
            "core": "counter <= counter + 1;\n        if counter < unsigned(din) then pwm_out <= '1'; else pwm_out <= '0'; end if;\n        int_data <= std_logic_vector(counter);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal pwm_out : std_logic;",
            "tb_map": "din => din, pwm_out => pwm_out,",
            "tb_stim": "din <= x\"0000_0005\"; wait for 100 ns;"
        },
        "tz_ctl_002_comp_pwm": {
            "ch": "16",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        pwm_h : out std_logic;\n        pwm_l : out std_logic",
            "signals": "signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);\n    signal p_base : std_logic;",
            "reset": "counter <= (others => '0'); pwm_h <= '0'; pwm_l <= '1'; p_base <= '0';",
            "core": "counter <= counter + 1;\n        if counter < unsigned(din) then p_base <= '1'; else p_base <= '0'; end if;\n        pwm_h <= p_base; pwm_l <= not p_base;\n        int_data(0) <= p_base;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal pwm_h, pwm_l : std_logic;",
            "tb_map": "din => din, pwm_h => pwm_h, pwm_l => pwm_l,",
            "tb_stim": "din <= x\"0000_000A\"; wait for 100 ns;"
        },
        "tz_ctl_003_dead_time": {
            "ch": "17",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        pwm_in : in std_logic;\n        pwm_h : out std_logic;\n        pwm_l : out std_logic",
            "signals": "signal d_reg : std_logic;",
            "reset": "d_reg <= '0'; pwm_h <= '0'; pwm_l <= '0';",
            "core": "d_reg <= pwm_in;\n        pwm_h <= d_reg; pwm_l <= not d_reg;\n        int_data(0) <= d_reg;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal pwm_in : std_logic := '0';\n    signal pwm_h, pwm_l : std_logic;",
            "tb_map": "din => din, pwm_in => pwm_in, pwm_h => pwm_h, pwm_l => pwm_l,",
            "tb_stim": "pwm_in <= '1'; wait for 50 ns; pwm_in <= '0'; wait for 50 ns;"
        },
        "tz_ctl_004_dc_motor": {
            "ch": "18",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        en : out std_logic;\n        dir1 : out std_logic;\n        dir2 : out std_logic",
            "signals": "",
            "reset": "en <= '0'; dir1 <= '0'; dir2 <= '0';",
            "core": "en <= din(0);\n        dir1 <= din(1);\n        dir2 <= not din(1);\n        int_data(1 downto 0) <= din(1 downto 0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal en, dir1, dir2 : std_logic;",
            "tb_map": "din => din, en => en, dir1 => dir1, dir2 => dir2,",
            "tb_stim": "din <= x\"0000_0003\"; wait for 50 ns; din <= x\"0000_0001\"; wait for 50 ns;"
        },
        "tz_ctl_005_stepper": {
            "ch": "19",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        step_out : out std_logic;\n        dir_out : out std_logic",
            "signals": "signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);\n    signal s_pulse : std_logic;",
            "reset": "counter <= (others => '0'); step_out <= '0'; dir_out <= '0'; s_pulse <= '0';",
            "core": "counter <= counter + 1;\n        if counter >= unsigned(din(30 downto 0)) then counter <= (others => '0'); s_pulse <= '1'; else s_pulse <= '0'; end if;\n        step_out <= s_pulse; dir_out <= din(31);\n        int_data(0) <= s_pulse;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal step_out, dir_out : std_logic;",
            "tb_map": "din => din, step_out => step_out, dir_out => dir_out,",
            "tb_stim": "din <= x\"8000_0005\"; wait for 100 ns;"
        },
        "tz_ctl_006_servo": {
            "ch": "1A",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        servo_pwm : out std_logic",
            "signals": "signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "counter <= (others => '0'); servo_pwm <= '0';",
            "core": "counter <= counter + 1;\n        if counter < unsigned(din) then servo_pwm <= '1'; else servo_pwm <= '0'; end if;\n        int_data <= std_logic_vector(counter);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal servo_pwm : std_logic;",
            "tb_map": "din => din, servo_pwm => servo_pwm,",
            "tb_stim": "din <= x\"0000_0008\"; wait for 100 ns;"
        },
        "tz_ctl_007_encoder": {
            "ch": "1B",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        enc_a : in std_logic;\n        enc_b : in std_logic",
            "signals": "signal a_d : std_logic;\n    signal count : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "a_d <= '0'; count <= (others => '0');",
            "core": "a_d <= enc_a;\n        if enc_a = '1' and a_d = '0' then\n            if enc_b = '1' then count <= count + 1; else count <= count - 1; end if;\n        end if;\n        int_data <= std_logic_vector(count);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal enc_a, enc_b : std_logic := '0';",
            "tb_map": "din => din, enc_a => enc_a, enc_b => enc_b,",
            "tb_stim": "enc_a <= '1'; enc_b <= '1'; wait for 20 ns; enc_a <= '0'; wait for 20 ns;"
        },
        "tz_ctl_008_pid": {
            "ch": "1C",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        fb_in : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        ctrl_out : out std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0)",
            "signals": "signal err : signed(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "ctrl_out <= (others => '0'); err <= (others => '0');",
            "core": "err <= signed(din) - signed(fb_in);\n        ctrl_out <= std_logic_vector(err);\n        int_data <= std_logic_vector(err);",
            "tb_sigs": "signal din, fb_in : std_logic_vector(31 downto 0) := (others => '0');\n    signal ctrl_out : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, fb_in => fb_in, ctrl_out => ctrl_out,",
            "tb_stim": "din <= x\"0000_0100\"; fb_in <= x\"0000_00F0\"; wait for 50 ns;"
        },
        "tz_ctl_009_watchdog": {
            "ch": "1D",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        wd_rst : out std_logic",
            "signals": "signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "counter <= (others => '0'); wd_rst <= '0';",
            "core": "if din(0) = '1' then counter <= (others => '0'); wd_rst <= '0';\n        else counter <= counter + 1; end if;\n        if counter > x\"0000_FFFF\" then wd_rst <= '1'; end if;\n        int_data <= std_logic_vector(counter);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal wd_rst : std_logic;",
            "tb_map": "din => din, wd_rst => wd_rst,",
            "tb_stim": "wait for 20 ns; din(0) <= '1'; wait for 10 ns; din(0) <= '0'; wait for 50 ns;"
        },
        "tz_ctl_010_counter": {
            "ch": "1E",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        pulse_in : in std_logic;\n        match_out : out std_logic",
            "signals": "signal p_d : std_logic;\n    signal count : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "p_d <= '0'; count <= (others => '0'); match_out <= '0';",
            "core": "p_d <= pulse_in;\n        if pulse_in = '1' and p_d = '0' then count <= count + 1; end if;\n        if count >= unsigned(din) then match_out <= '1'; else match_out <= '0'; end if;\n        int_data <= std_logic_vector(count);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := x\"0000_0002\";\n    signal pulse_in : std_logic := '0';\n    signal match_out : std_logic;",
            "tb_map": "din => din, pulse_in => pulse_in, match_out => match_out,",
            "tb_stim": "pulse_in <= '1'; wait for 20 ns; pulse_in <= '0'; wait for 20 ns; pulse_in <= '1'; wait for 20 ns; pulse_in <= '0'; wait for 20 ns;"
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

    print("Iniciando Injecao Blindada na Familia TZ-03-CTL...")
    
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
            
        print(f" -> Logica de Controle injetada em: {ip}")
        
    print("Injecao da Familia 03 (Controle) concluida!")

if __name__ == "__main__":
    main()