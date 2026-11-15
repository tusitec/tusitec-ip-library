library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_010_widthconv is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        data_16bit  : in  std_logic_vector(15 downto 0);
        data_valid  : in  std_logic;
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_010_widthconv is
    signal buffer_reg : std_logic_vector(15 downto 0);
    signal toggle     : std_logic;
    signal valid_flag : std_logic;
    signal data_out   : std_logic_vector(31 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            buffer_reg <= (others => '0');
            toggle     <= '0';
            valid_flag <= '0';
            data_out   <= (others => '0');
        elsif rising_edge(clk) then
            valid_flag <= '0';
            if data_valid = '1' then
                if toggle = '0' then
                    buffer_reg <= data_16bit; -- Guarda a primeira metade (MSB)
                    toggle <= '1';
                else
                    data_out <= buffer_reg & data_16bit; -- Concatena a segunda metade (LSB) e dispara
                    valid_flag <= '1';
                    toggle <= '0';
                end if;
            end if;
        end if;
    end process;

    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= data_out;
    tlink_tx.channel <= x"0A";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;