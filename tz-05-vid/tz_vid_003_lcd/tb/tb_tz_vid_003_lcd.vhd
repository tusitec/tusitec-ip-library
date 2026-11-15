library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_vid_003_lcd is
end entity;

architecture sim of tb_tz_vid_003_lcd is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal lcd_rs, lcd_en : std_logic;
    signal lcd_data : std_logic_vector(7 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_vid_003_lcd
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, lcd_rs => lcd_rs, lcd_en => lcd_en, lcd_data => lcd_data,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din <= x"0000_0341"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
