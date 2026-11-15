library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_ctl_005_stepper is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        step_out : out std_logic;
        dir_out : out std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_ctl_005_stepper is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    signal counter : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);
    signal s_pulse : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            counter <= (others => '0'); step_out <= '0'; dir_out <= '0'; s_pulse <= '0';
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            counter <= counter + 1;
        if counter >= unsigned(din(30 downto 0)) then counter <= (others => '0'); s_pulse <= '1'; else s_pulse <= '0'; end if;
        step_out <= s_pulse; dir_out <= din(31);
        int_data(0) <= s_pulse;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"19";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
