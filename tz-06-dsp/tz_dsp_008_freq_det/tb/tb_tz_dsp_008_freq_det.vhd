library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_dsp_008_freq_det is
end entity;

architecture sim of tb_tz_dsp_008_freq_det is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal sig_in : std_logic := '0';
    signal freq_out : std_logic_vector(31 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_dsp_008_freq_det
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, sig_in => sig_in, freq_out => freq_out,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        sig_in <= '1'; wait for 20 ns; sig_in <= '0'; wait for 50 ns; sig_in <= '1'; wait for 20 ns; sig_in <= '0';
        wait;
    end process;
end architecture sim;
