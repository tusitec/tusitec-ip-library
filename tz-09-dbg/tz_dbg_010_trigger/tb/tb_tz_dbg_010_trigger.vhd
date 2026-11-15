library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_dbg_010_trigger is
end entity;

architecture sim of tb_tz_dbg_010_trigger is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal trig_in : std_logic := '0';
    signal trig_out : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_dbg_010_trigger
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, trig_in => trig_in, trig_out => trig_out,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        trig_in <= '1'; wait for 10 ns; trig_in <= '0'; wait for 40 ns; din <= x"0000_0001"; wait for 20 ns;
        wait;
    end process;
end architecture sim;
