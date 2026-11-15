library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_dbg_001_logic_ana is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        probe_in : in std_logic_vector(15 downto 0);
        trigger_match : out std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_dbg_001_logic_ana is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    signal trig_val : std_logic_vector(15 downto 0);
    signal match_reg : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            trig_val <= (others => '0'); match_reg <= '0'; trigger_match <= '0';
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            trig_val <= din(15 downto 0);
        if probe_in = trig_val then match_reg <= '1'; else match_reg <= '0'; end if;
        trigger_match <= match_reg;
        int_data(15 downto 0) <= probe_in;
        int_data(16) <= match_reg;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"51";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
