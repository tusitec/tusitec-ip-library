library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_aqd_004_ana_acq is
end entity;

architecture sim of tb_tz_aqd_004_ana_acq is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal start_conv : std_logic;
    signal adc_data : std_logic_vector(15 downto 0) := x"0000";
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_aqd_004_ana_acq
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, start_conv => start_conv, adc_data => adc_data,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din(0) <= '1'; adc_data <= x"1234"; wait for 20 ns; din(0) <= '0'; wait for 20 ns;
        wait;
    end process;
end architecture sim;
