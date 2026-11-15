library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_log_004_shiftreg is
end entity;

architecture sim of tb_tz_log_004_shiftreg is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal shift_en, ser_in : std_logic := '0';
    signal par_out : std_logic_vector(31 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    dut: entity work.tz_log_004_shiftreg
        port map (
            clk      => clk,
            rst_n    => rst_n,
            shift_en => shift_en, ser_in => ser_in, par_out => par_out,
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
        
        ser_in <= '1'; shift_en <= '1'; wait for 10 ns; shift_en <= '0'; wait for 20 ns;
        
        wait;
    end process;
end architecture sim;
