library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_009_pulsegen is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        trigger     : in  std_logic;
        width_cfg   : in  std_logic_vector(31 downto 0);
        pulse_out   : out std_logic;
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_009_pulsegen is
    signal counter : unsigned(31 downto 0);
    signal active  : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            counter   <= (others => '0');
            active    <= '0';
            pulse_out <= '0';
        elsif rising_edge(clk) then
            if trigger = '1' and active = '0' then
                active  <= '1';
                counter <= unsigned(width_cfg);
                pulse_out <= '1';
            elsif active = '1' then
                if counter = 1 then
                    active <= '0';
                    pulse_out <= '0';
                else
                    counter <= counter - 1;
                end if;
            end if;
        end if;
    end process;

    tlink_tx.valid   <= active; -- Reporta ao Hub enquanto o pulso estiver ocorrendo
    tlink_tx.data    <= std_logic_vector(counter);
    tlink_tx.channel <= x"09";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;