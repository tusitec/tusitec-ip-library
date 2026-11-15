library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_mem_004_async_fifo is
end entity;

architecture sim of tb_tz_mem_004_async_fifo is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal rd_clk, wr_en, rd_en : std_logic := '0';
    signal dout : std_logic_vector(31 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_mem_004_async_fifo
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, rd_clk => rd_clk, wr_en => wr_en, rd_en => rd_en, dout => dout,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        rd_clk <= clk; din <= x"2222_2222"; wr_en <= '1'; wait for 20 ns; wr_en <= '0'; rd_en <= '1'; wait for 20 ns; rd_en <= '0';
        wait;
    end process;
end architecture sim;
