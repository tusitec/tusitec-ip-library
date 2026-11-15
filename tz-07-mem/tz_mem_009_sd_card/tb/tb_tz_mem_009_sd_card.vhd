library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_mem_009_sd_card is
end entity;

architecture sim of tb_tz_mem_009_sd_card is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal sd_clk : std_logic;
    signal sd_cmd : std_logic;
    signal sd_dat : std_logic_vector(3 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_mem_009_sd_card
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, sd_clk => sd_clk, sd_cmd => sd_cmd, sd_dat => sd_dat,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din <= x"0000_0000"; wait for 50 ns; din <= x"0000_0007"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
