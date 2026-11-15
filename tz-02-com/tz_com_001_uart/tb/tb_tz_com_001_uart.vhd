library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_com_001_uart is
end entity;

architecture sim of tb_tz_com_001_uart is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal tx : std_logic;
    signal rx : std_logic := '1';
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_com_001_uart
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, tx => tx, rx => rx,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din <= x"0000_0000"; rx <= '0'; wait for 20 ns; rx <= '1';
        wait;
    end process;
end architecture sim;
