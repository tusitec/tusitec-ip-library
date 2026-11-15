import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-10-esp"
    
    # Dicionário VHDL estrito para os 10 IPs Especiais (Vanguarda Tecnológica)
    ips = {
        "tz_esp_001_sensor_fusion": {
            "ch": "5B",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        sensor_a : in std_logic_vector(15 downto 0);\n        sensor_b : in std_logic_vector(15 downto 0);\n        fused_out : out std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "fused_out <= (others => '0');",
            "core": "fused_out <= sensor_a & sensor_b;\n        int_data <= sensor_a & sensor_b;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal sensor_a, sensor_b : std_logic_vector(15 downto 0) := (others => '0');\n    signal fused_out : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, sensor_a => sensor_a, sensor_b => sensor_b, fused_out => fused_out,",
            "tb_stim": "sensor_a <= x\"AAAA\"; sensor_b <= x\"BBBB\"; wait for 50 ns;"
        },
        "tz_esp_002_robotics": {
            "ch": "5C",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        kinematics_in : in std_logic_vector(15 downto 0);\n        motor_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "motor_out <= (others => '0');",
            "core": "motor_out <= kinematics_in;\n        int_data(15 downto 0) <= kinematics_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal kinematics_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal motor_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, kinematics_in => kinematics_in, motor_out => motor_out,",
            "tb_stim": "kinematics_in <= x\"1234\"; wait for 50 ns;"
        },
        "tz_esp_003_auto_nav": {
            "ch": "5D",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        gps_in : in std_logic_vector(15 downto 0);\n        imu_in : in std_logic_vector(15 downto 0);\n        waypoint_out : out std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "waypoint_out <= (others => '0');",
            "core": "waypoint_out <= gps_in & imu_in;\n        int_data <= gps_in & imu_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal gps_in, imu_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal waypoint_out : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, gps_in => gps_in, imu_in => imu_in, waypoint_out => waypoint_out,",
            "tb_stim": "gps_in <= x\"4321\"; imu_in <= x\"8765\"; wait for 50 ns;"
        },
        "tz_esp_004_aes": {
            "ch": "5E",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        plaintext : in std_logic_vector(31 downto 0);\n        key_in : in std_logic_vector(31 downto 0);\n        ciphertext : out std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "ciphertext <= (others => '0');",
            "core": "ciphertext <= plaintext xor key_in;\n        int_data <= plaintext xor key_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal plaintext, key_in : std_logic_vector(31 downto 0) := (others => '0');\n    signal ciphertext : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, plaintext => plaintext, key_in => key_in, ciphertext => ciphertext,",
            "tb_stim": "plaintext <= x\"11112222\"; key_in <= x\"FFFF0000\"; wait for 50 ns;"
        },
        "tz_esp_005_err_corr": {
            "ch": "5F",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        data_in : in std_logic_vector(15 downto 0);\n        data_out : out std_logic_vector(15 downto 0);\n        err_flag : out std_logic",
            "signals": "",
            "reset": "data_out <= (others => '0'); err_flag <= '0';",
            "core": "data_out <= data_in;\n        err_flag <= din(0);\n        int_data(15 downto 0) <= data_in;\n        int_data(16) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal data_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal data_out : std_logic_vector(15 downto 0);\n    signal err_flag : std_logic;",
            "tb_map": "din => din, data_in => data_in, data_out => data_out, err_flag => err_flag,",
            "tb_stim": "data_in <= x\"ABCD\"; din <= x\"00000001\"; wait for 50 ns;"
        },
        "tz_esp_006_cv_engine": {
            "ch": "60",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        pixel_in : in std_logic_vector(7 downto 0);\n        feature_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "feature_out <= (others => '0');",
            "core": "feature_out <= pixel_in & pixel_in;\n        int_data(15 downto 0) <= pixel_in & pixel_in;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal pixel_in : std_logic_vector(7 downto 0) := (others => '0');\n    signal feature_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, pixel_in => pixel_in, feature_out => feature_out,",
            "tb_stim": "pixel_in <= x\"7F\"; wait for 50 ns;"
        },
        "tz_esp_007_ind_net": {
            "ch": "61",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        fieldbus_rx : in std_logic;\n        fieldbus_tx : out std_logic",
            "signals": "",
            "reset": "fieldbus_tx <= '0';",
            "core": "fieldbus_tx <= din(0);\n        int_data(0) <= fieldbus_rx;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal fieldbus_rx : std_logic := '0';\n    signal fieldbus_tx : std_logic;",
            "tb_map": "din => din, fieldbus_rx => fieldbus_rx, fieldbus_tx => fieldbus_tx,",
            "tb_stim": "fieldbus_rx <= '1'; din <= x\"00000001\"; wait for 50 ns;"
        },
        "tz_esp_008_sci_inst": {
            "ch": "62",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        analog_sample : in std_logic_vector(15 downto 0);\n        processed_val : out std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "processed_val <= (others => '0');",
            "core": "processed_val <= x\"0000\" & analog_sample;\n        int_data <= x\"0000\" & analog_sample;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal analog_sample : std_logic_vector(15 downto 0) := (others => '0');\n    signal processed_val : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, analog_sample => analog_sample, processed_val => processed_val,",
            "tb_stim": "analog_sample <= x\"FFFF\"; wait for 50 ns;"
        },
        "tz_esp_009_telecom_dsp": {
            "ch": "63",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        iq_in : in std_logic_vector(31 downto 0);\n        sym_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "sym_out <= (others => '0');",
            "core": "sym_out <= iq_in(15 downto 0) xor iq_in(31 downto 16);\n        int_data(15 downto 0) <= iq_in(15 downto 0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal iq_in : std_logic_vector(31 downto 0) := (others => '0');\n    signal sym_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, iq_in => iq_in, sym_out => sym_out,",
            "tb_stim": "iq_in <= x\"0F0F00FF\"; wait for 50 ns;"
        },
        "tz_esp_010_nn_accel": {
            "ch": "64",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        activation_in : in std_logic_vector(15 downto 0);\n        weight_in : in std_logic_vector(15 downto 0);\n        mac_out : out std_logic_vector(31 downto 0)",
            "signals": "",
            "reset": "mac_out <= (others => '0');",
            "core": "mac_out <= std_logic_vector(unsigned(activation_in) * unsigned(weight_in));\n        int_data <= std_logic_vector(unsigned(activation_in) * unsigned(weight_in));",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal activation_in, weight_in : std_logic_vector(15 downto 0) := (others => '0');\n    signal mac_out : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, activation_in => activation_in, weight_in => weight_in, mac_out => mac_out,",
            "tb_stim": "activation_in <= x\"0002\"; weight_in <= x\"0003\"; wait for 50 ns;"
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

    print("A iniciar Injeção Blindada na Família TZ-10-ESP...")
    
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
            
        print(f" -> Lógica Especializada injetada em: {ip}")
        
    print("Injeção da Família 10 (Especiais) concluída!")

if __name__ == "__main__":
    main()