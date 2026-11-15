library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_aqd_003_dig_sensor is
end entity;

architecture sim of tb_tz_aqd_003_dig_sensor is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal sensor_in : std_logic := '0';
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_aqd_003_dig_sensor
        port map (
            clk      => clk,
            rst_n    => rst_n,
            sensor_in => sensor_in,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        sensor_in <= '1'; wait for 30 ns; sensor_in <= '0'; wait for 30 ns;
        wait;
    end process;
end architecture sim;
