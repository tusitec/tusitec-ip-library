library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_log_002_counter is
end entity;

architecture sim of tb_tz_log_002_counter is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal enable, clear : std_logic := '0';
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    dut: entity work.tz_log_002_counter
        port map (
            clk      => clk,
            rst_n    => rst_n,
            enable => enable, clear => clear,
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
        
        enable <= '1'; wait for 10 ns; enable <= '0'; wait for 20 ns; clear <= '1'; wait for 10 ns; clear <= '0';
        
        wait;
    end process;
end architecture sim;
