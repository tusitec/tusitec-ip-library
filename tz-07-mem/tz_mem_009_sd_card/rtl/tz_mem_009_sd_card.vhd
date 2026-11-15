library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_009_sd_card is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sd_clk : out std_logic;
        sd_cmd : inout std_logic;
        sd_dat : inout std_logic_vector(3 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_009_sd_card is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            sd_clk <= '0'; sd_cmd <= 'Z'; sd_dat <= (others => 'Z');
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            sd_clk <= clk;
        if din(0) = '1' then sd_cmd <= din(1); else sd_cmd <= 'Z'; end if;
        if din(2) = '1' then sd_dat <= din(6 downto 3); else sd_dat <= (others => 'Z'); end if;
        if sd_cmd = 'H' or sd_cmd = '1' then int_data(0) <= '1'; else int_data(0) <= '0'; end if;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"45";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
