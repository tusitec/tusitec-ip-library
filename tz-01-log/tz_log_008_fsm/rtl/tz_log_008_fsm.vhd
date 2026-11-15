library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_008_fsm is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- INTERFACE FISICA DO IP
        start : in std_logic;
        done : out std_logic;
        state_out : out std_logic_vector(3 downto 0);
        
        -- INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_008_fsm is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
    signal state_reg : std_logic_vector(3 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            internal_data <= (others => '0');
            state_reg <= "0000";
        elsif rising_edge(clk) then
            internal_data <= (others => '0'); 
            if start = '1' then state_reg <= "0001"; elsif state_reg = "0001" then state_reg <= "0010"; elsif state_reg = "0010" then state_reg <= "0100"; else state_reg <= "0000"; end if;
        if state_reg = "0100" then done <= '1'; else done <= '0'; end if;
        state_out <= state_reg; internal_data(3 downto 0) <= state_reg;
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
    tlink_tx.channel <= x"08"; 
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
