library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_com_009_eth_mac is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        mdc : out std_logic;
        mdio : inout std_logic;
        rxd : in std_logic_vector(1 downto 0);
        txd : out std_logic_vector(1 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_com_009_eth_mac is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            mdc <= '0'; mdio <= 'Z'; txd <= "00";
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            mdc <= clk;
        txd <= din(1 downto 0);
        int_data(1 downto 0) <= rxd;
        int_data(2) <= mdio;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"13";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
