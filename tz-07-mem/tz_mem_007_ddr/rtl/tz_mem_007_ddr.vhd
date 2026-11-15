library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_007_ddr is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        ddr_ck : out std_logic;
        ddr_ck_n : out std_logic;
        ddr_cke : out std_logic;
        ddr_cs_n : out std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_007_ddr is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            ddr_ck <= '0'; ddr_ck_n <= '1'; ddr_cke <= '0'; ddr_cs_n <= '1';
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            ddr_ck <= clk; ddr_ck_n <= not clk;
        ddr_cke <= din(0);
        ddr_cs_n <= din(1);
        int_data(0) <= din(0);
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"43";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
