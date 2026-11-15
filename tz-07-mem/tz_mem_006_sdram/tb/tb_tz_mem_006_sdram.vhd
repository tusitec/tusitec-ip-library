library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_mem_006_sdram is
end entity;

architecture sim of tb_tz_mem_006_sdram is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal sdram_clk, sdram_cke, sdram_cs_n, sdram_ras_n, sdram_cas_n, sdram_we_n : std_logic;
    signal sdram_addr : std_logic_vector(12 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_mem_006_sdram
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, sdram_clk => sdram_clk, sdram_cke => sdram_cke, sdram_cs_n => sdram_cs_n, sdram_ras_n => sdram_ras_n, sdram_cas_n => sdram_cas_n, sdram_we_n => sdram_we_n, sdram_addr => sdram_addr,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din <= x"0000_001F"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
