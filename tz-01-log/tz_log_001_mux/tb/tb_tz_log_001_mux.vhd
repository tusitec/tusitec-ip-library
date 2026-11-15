library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_log_001_mux is
end entity;

architecture sim of tb_tz_log_001_mux is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal sel : std_logic := '0';
    signal din_a, din_b : std_logic_vector(31 downto 0) := (others => '0');
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    dut: entity work.tz_log_001_mux
        port map (
            clk      => clk,
            rst_n    => rst_n,
            sel => sel, din_a => din_a, din_b => din_b,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    stim_proc: process
    begin
        rst_n <= '0';
        tlink_rx.ready <= '0';
        wait for 20 ns;
        rst_n <= '1';
        wait for 20 ns;
        tlink_rx.ready <= '1';
        
        din_a <= x"AAAA_0000"; din_b <= x"BBBB_1111"; sel <= '0'; wait for 50 ns; sel <= '1'; wait for 50 ns;
        
        wait;
    end process;
end architecture sim;
