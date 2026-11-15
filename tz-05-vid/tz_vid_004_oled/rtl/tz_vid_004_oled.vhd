library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_vid_004_oled is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        oled_sck : out std_logic;
        oled_sda : out std_logic;
        oled_dc : out std_logic;
        oled_cs : out std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_vid_004_oled is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            oled_sck <= '0'; oled_sda <= '0'; oled_dc <= '0'; oled_cs <= '1';
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            oled_sck <= clk;
        oled_sda <= din(0);
        oled_dc <= din(1);
        oled_cs <= din(2);
        int_data(0) <= din(0);
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"2C";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
