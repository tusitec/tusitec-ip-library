library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_aqd_007_per_meter is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        sig_in : in std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_aqd_007_per_meter is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    signal p_d : std_logic;
    signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            p_d <= '0'; counter <= (others => '0');
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            p_d <= sig_in;
        if sig_in = '1' and p_d = '0' then int_data <= std_logic_vector(counter); counter <= (others => '0');
        else counter <= counter + 1; end if;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"25";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
