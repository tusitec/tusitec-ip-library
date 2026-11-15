library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_006_sdram is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sdram_clk : out std_logic;
        sdram_cke : out std_logic;
        sdram_cs_n : out std_logic;
        sdram_ras_n : out std_logic;
        sdram_cas_n : out std_logic;
        sdram_we_n : out std_logic;
        sdram_addr : out std_logic_vector(12 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_006_sdram is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            sdram_clk <= '0'; sdram_cke <= '0'; sdram_cs_n <= '1'; sdram_ras_n <= '1'; sdram_cas_n <= '1'; sdram_we_n <= '1'; sdram_addr <= (others => '0');
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            sdram_clk <= clk;
        sdram_cke <= din(0);
        sdram_cs_n <= din(1);
        sdram_ras_n <= din(2);
        sdram_cas_n <= din(3);
        sdram_we_n <= din(4);
        sdram_addr <= din(17 downto 5);
        int_data(0) <= din(0);
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"42";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
