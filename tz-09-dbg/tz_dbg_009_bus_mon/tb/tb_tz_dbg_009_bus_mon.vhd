library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_dbg_009_bus_mon is
end entity;

architecture sim of tb_tz_dbg_009_bus_mon is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal bus_valid : std_logic := '0';
    signal bus_data : std_logic_vector(31 downto 0) := (others => '0');
    signal err_flag : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_dbg_009_bus_mon
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, bus_valid => bus_valid, bus_data => bus_data, err_flag => err_flag,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        bus_valid <= '1'; bus_data <= x"12345678"; wait for 20 ns; bus_data <= x"00000000"; wait for 20 ns; bus_valid <= '0'; wait for 20 ns;
        wait;
    end process;
end architecture sim;
