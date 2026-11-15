library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_009_pulsegen is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- INTERFACE FISICA DO IP
        trigger : in std_logic;
        pulse_ticks : in std_logic_vector(15 downto 0);
        pulse_out : out std_logic;
        
        -- INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_009_pulsegen is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
    signal counter : unsigned(15 downto 0);
    signal active : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            internal_data <= (others => '0');
            counter <= (others => '0'); active <= '0';
        elsif rising_edge(clk) then
            internal_data <= (others => '0'); 
            if trigger = '1' and active = '0' then active <= '1'; counter <= unsigned(pulse_ticks); elsif active = '1' then if counter = 0 then active <= '0'; else counter <= counter - 1; end if; end if;
        pulse_out <= active; internal_data(0) <= active;
        end if;
    end process;

    process(clk, rst_n)
    begin
        if rst_n = '0' then
            valid_flag <= '0';
        elsif rising_edge(clk) then
            valid_flag <= '1';
        end if;
    end process;

    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= internal_data;
    tlink_tx.channel <= x"09"; 
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
