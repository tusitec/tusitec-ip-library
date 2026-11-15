library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_dsp_005_mac is
end entity;

architecture sim of tb_tz_dsp_005_mac is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal a_in, b_in : std_logic_vector(15 downto 0) := (others => '0');
    signal acc_out : std_logic_vector(31 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_dsp_005_mac
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, a_in => a_in, b_in => b_in, acc_out => acc_out,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        a_in <= x"0002"; b_in <= x"0003"; wait for 50 ns; din(0) <= '1'; wait for 20 ns; din(0) <= '0';
        wait;
    end process;
end architecture sim;
