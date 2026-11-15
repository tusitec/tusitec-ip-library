library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_dsp_004_ifft is
end entity;

architecture sim of tb_tz_dsp_004_ifft is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal real_in, imag_in : std_logic_vector(15 downto 0) := (others => '0');
    signal real_out, imag_out : std_logic_vector(15 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_dsp_004_ifft
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, real_in => real_in, imag_in => imag_in, real_out => real_out, imag_out => imag_out,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        real_in <= x"0300"; imag_in <= x"0400"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
