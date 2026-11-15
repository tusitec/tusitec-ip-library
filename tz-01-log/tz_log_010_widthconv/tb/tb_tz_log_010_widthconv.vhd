library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_log_010_widthconv is
end entity;

architecture sim of tb_tz_log_010_widthconv is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din_8bit : std_logic_vector(7 downto 0) := x"AA";
    signal dout_32bit : std_logic_vector(31 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    dut: entity work.tz_log_010_widthconv
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din_8bit => din_8bit, dout_32bit => dout_32bit,
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
        
        din_8bit <= x"FF"; wait for 30 ns; din_8bit <= x"12"; wait for 30 ns;
        
        wait;
    end process;
end architecture sim;
