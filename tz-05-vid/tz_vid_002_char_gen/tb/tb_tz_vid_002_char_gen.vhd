library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_vid_002_char_gen is
end entity;

architecture sim of tb_tz_vid_002_char_gen is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal char_code : std_logic_vector(7 downto 0) := x"00";
    signal pixel_out : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_vid_002_char_gen
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, char_code => char_code, pixel_out => pixel_out,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din <= x"0000_0001"; char_code <= x"41"; wait for 50 ns; char_code <= x"42"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
