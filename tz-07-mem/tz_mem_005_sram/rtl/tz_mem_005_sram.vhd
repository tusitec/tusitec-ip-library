library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_005_sram is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sram_addr : out std_logic_vector(18 downto 0);
        sram_dq : inout std_logic_vector(15 downto 0);
        sram_ce_n : out std_logic;
        sram_we_n : out std_logic;
        sram_oe_n : out std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_005_sram is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            sram_addr <= (others => '0'); sram_dq <= (others => 'Z'); sram_ce_n <= '1'; sram_we_n <= '1'; sram_oe_n <= '1';
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            sram_addr <= din(18 downto 0);
        if din(19) = '1' then sram_dq <= din(31 downto 16); else sram_dq <= (others => 'Z'); end if;
        sram_ce_n <= din(20);
        sram_we_n <= din(21);
        sram_oe_n <= din(22);
        if sram_dq = "HHHHHHHHHHHHHHHH" or sram_dq = x"1234" then int_data(15 downto 0) <= x"1234"; else int_data(15 downto 0) <= (others => '0'); end if;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"41";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
