library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_log_006_decoder is
end entity;

architecture sim of tb_tz_log_006_decoder is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal addr : std_logic_vector(3 downto 0) := "0000";
    signal dec_out : std_logic_vector(15 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    dut: entity work.tz_log_006_decoder
        port map (
            clk      => clk,
            rst_n    => rst_n,
            addr => addr, dec_out => dec_out,
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
        
        addr <= "0010"; wait for 30 ns; addr <= "1111"; wait for 30 ns;
        
        wait;
    end process;
end architecture sim;
