library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_dbg_003_test_sig is
end entity;

architecture sim of tb_tz_dbg_003_test_sig is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal sig_out : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_dbg_003_test_sig
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, sig_out => sig_out,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din <= x"0000_0001"; wait for 50 ns; din <= x"0000_0000"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
