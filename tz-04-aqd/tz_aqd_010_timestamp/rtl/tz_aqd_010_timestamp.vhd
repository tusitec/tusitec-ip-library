library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_aqd_010_timestamp is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        event_in : in std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_aqd_010_timestamp is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    signal time_reg : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);
    signal e_d : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            time_reg <= (others => '0'); e_d <= '0';
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            time_reg <= time_reg + 1;
        e_d <= event_in;
        if event_in = '1' and e_d = '0' then int_data <= std_logic_vector(time_reg); end if;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"28";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
