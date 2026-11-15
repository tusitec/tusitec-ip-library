import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-06-dsp"
    
    # Dicionário VHDL estrito para os 10 IPs de DSP
    ips = {
        "tz_dsp_001_fir": {
            "ch": "33",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        x_in : in std_logic_vector(15 downto 0);\n        y_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "y_out <= (others => '0');",
            "core": "y_out <= x_in;\n        int_data(15 downto 0) <= x_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal x_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal y_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, x_in => x_in, y_out => y_out,",
            "tb_stim": "x_in <= x\"1000\"; wait for 50 ns;"
        },
        "tz_dsp_002_iir": {
            "ch": "34",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        x_in : in std_logic_vector(15 downto 0);\n        y_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "y_out <= (others => '0');",
            "core": "y_out <= x_in;\n        int_data(15 downto 0) <= x_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal x_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal y_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, x_in => x_in, y_out => y_out,",
            "tb_stim": "x_in <= x\"2000\"; wait for 50 ns;"
        },
        "tz_dsp_003_fft": {
            "ch": "35",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        real_in : in std_logic_vector(15 downto 0);\n        imag_in : in std_logic_vector(15 downto 0);\n        real_out : out std_logic_vector(15 downto 0);\n        imag_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "real_out <= (others => '0'); imag_out <= (others => '0');",
            "core": "real_out <= real_in; imag_out <= imag_in;\n        int_data(15 downto 0) <= real_in;\n        int_data(31 downto 16) <= imag_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal real_in, imag_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal real_out, imag_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, real_in => real_in, imag_in => imag_in, real_out => real_out, imag_out => imag_out,",
            "tb_stim": "real_in <= x\"0100\"; imag_in <= x\"0200\"; wait for 50 ns;"
        },
        "tz_dsp_004_ifft": {
            "ch": "36",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        real_in : in std_logic_vector(15 downto 0);\n        imag_in : in std_logic_vector(15 downto 0);\n        real_out : out std_logic_vector(15 downto 0);\n        imag_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "real_out <= (others => '0'); imag_out <= (others => '0');",
            "core": "real_out <= real_in; imag_out <= imag_in;\n        int_data(15 downto 0) <= real_in;\n        int_data(31 downto 16) <= imag_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal real_in, imag_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal real_out, imag_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, real_in => real_in, imag_in => imag_in, real_out => real_out, imag_out => imag_out,",
            "tb_stim": "real_in <= x\"0300\"; imag_in <= x\"0400\"; wait for 50 ns;"
        },
        "tz_dsp_005_mac": {
            "ch": "37",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        a_in : in std_logic_vector(15 downto 0);\n        b_in : in std_logic_vector(15 downto 0);\n        acc_out : out std_logic_vector(31 downto 0)",
            "signals": "signal acc_reg : unsigned(31 downto 0);",
            "reset": "acc_reg <= (others => '0'); acc_out <= (others => '0');",
            "core": "if din(0) = '1' then acc_reg <= (others => '0');\n        else acc_reg <= acc_reg + (unsigned(a_in) * unsigned(b_in)); end if;\n        acc_out <= std_logic_vector(acc_reg);\n        int_data <= std_logic_vector(acc_reg);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal a_in, b_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal acc_out : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, a_in => a_in, b_in => b_in, acc_out => acc_out,",
            "tb_stim": "a_in <= x\"0002\"; b_in <= x\"0003\"; wait for 50 ns; din(0) <= '1'; wait for 20 ns; din(0) <= '0';"
        },
        "tz_dsp_006_dds": {
            "ch": "38",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        phase_inc : in std_logic_vector(31 downto 0);\n        sine_out : out std_logic_vector(15 downto 0)",
            "signals": "signal phase_acc : unsigned(31 downto 0);",
            "reset": "phase_acc <= (others => '0'); sine_out <= (others => '0');",
            "core": "phase_acc <= phase_acc + unsigned(phase_inc);\n        sine_out <= std_logic_vector(phase_acc(31 downto 16));\n        int_data(15 downto 0) <= std_logic_vector(phase_acc(31 downto 16));",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal phase_inc : std_logic_vector(31 downto 0) := (others => '0');\n    signal sine_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, phase_inc => phase_inc, sine_out => sine_out,",
            "tb_stim": "phase_inc <= x\"0010_0000\"; wait for 100 ns;"
        },
        "tz_dsp_007_cordic": {
            "ch": "39",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        angle_in : in std_logic_vector(15 downto 0);\n        sin_out : out std_logic_vector(15 downto 0);\n        cos_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "sin_out <= (others => '0'); cos_out <= (others => '0');",
            "core": "sin_out <= angle_in; cos_out <= not angle_in;\n        int_data(15 downto 0) <= angle_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal angle_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal sin_out, cos_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, angle_in => angle_in, sin_out => sin_out, cos_out => cos_out,",
            "tb_stim": "angle_in <= x\"0F0F\"; wait for 50 ns;"
        },
        "tz_dsp_008_freq_det": {
            "ch": "3A",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        sig_in : in std_logic;\n        freq_out : out std_logic_vector(31 downto 0)",
            "signals": "signal s_d : std_logic;\n    signal cnt : unsigned(31 downto 0);",
            "reset": "s_d <= '0'; cnt <= (others => '0'); freq_out <= (others => '0');",
            "core": "s_d <= sig_in;\n        if sig_in = '1' and s_d = '0' then\n            freq_out <= std_logic_vector(cnt); cnt <= (others => '0');\n        else cnt <= cnt + 1; end if;\n        int_data <= std_logic_vector(cnt);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal sig_in : std_logic := '0';\n    signal freq_out : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, sig_in => sig_in, freq_out => freq_out,",
            "tb_stim": "sig_in <= '1'; wait for 20 ns; sig_in <= '0'; wait for 50 ns; sig_in <= '1'; wait for 20 ns; sig_in <= '0';"
        },
        "tz_dsp_009_modulator": {
            "ch": "3B",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        carrier_in : in std_logic_vector(15 downto 0);\n        msg_in : in std_logic_vector(15 downto 0);\n        mod_out : out std_logic_vector(15 downto 0)",
            "signals": "signal mult : unsigned(31 downto 0);",
            "reset": "mod_out <= (others => '0'); mult <= (others => '0');",
            "core": "mult <= unsigned(carrier_in) * unsigned(msg_in);\n        mod_out <= std_logic_vector(mult(31 downto 16));\n        int_data(15 downto 0) <= std_logic_vector(mult(31 downto 16));",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal carrier_in, msg_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal mod_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, carrier_in => carrier_in, msg_in => msg_in, mod_out => mod_out,",
            "tb_stim": "carrier_in <= x\"1000\"; msg_in <= x\"0002\"; wait for 50 ns;"
        },
        "tz_dsp_010_demodulator": {
            "ch": "3C",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        mod_in : in std_logic_vector(15 downto 0);\n        carrier_ref : in std_logic_vector(15 downto 0);\n        msg_out : out std_logic_vector(15 downto 0)",
            "signals": "signal mult : unsigned(31 downto 0);",
            "reset": "msg_out <= (others => '0'); mult <= (others => '0');",
            "core": "mult <= unsigned(mod_in) * unsigned(carrier_ref);\n        msg_out <= std_logic_vector(mult(31 downto 16));\n        int_data(15 downto 0) <= std_logic_vector(mult(31 downto 16));",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal mod_in, carrier_ref : std_logic_vector(15 downto 0) := (others => '0');\n    signal msg_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, mod_in => mod_in, carrier_ref => carrier_ref, msg_out => msg_out,",
            "tb_stim": "mod_in <= x\"2000\"; carrier_ref <= x\"0002\"; wait for 50 ns;"
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

    print("A iniciar Injeção Blindada na Família TZ-06-DSP...")
    
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
            
        print(f" -> DSP injetado com sucesso em: {ip}")
        
    print("Injeção da Família 06 (DSP) concluída!")

if __name__ == "__main__":
    main()