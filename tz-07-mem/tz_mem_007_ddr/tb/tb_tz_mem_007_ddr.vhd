library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_mem_007_ddr is
end entity;

architecture sim of tb_tz_mem_007_ddr is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal ddr_ck, ddr_ck_n, ddr_cke, ddr_cs_n : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_mem_007_ddr
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, ddr_ck => ddr_ck, ddr_ck_n => ddr_ck_n, ddr_cke => ddr_cke, ddr_cs_n => ddr_cs_n,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din <= x"0000_0001"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
