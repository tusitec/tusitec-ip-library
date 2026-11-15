library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_006_decoder is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        sel_in      : in  std_logic_vector(4 downto 0); -- Seleciona 1 entre 32
        enable      : in  std_logic;
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_006_decoder is
    signal decoded_out : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag  : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            decoded_out <= (others => '0');
            valid_flag  <= '0';
        elsif rising_edge(clk) then
            if enable = '1' then
                decoded_out <= (others => '0');
                decoded_out(to_integer(unsigned(sel_in))) <= '1';
                valid_flag  <= '1';
            else
                decoded_out <= (others => '0');
                valid_flag  <= '0';
            end if;
        end if;
    end process;

    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= decoded_out;
    tlink_tx.channel <= x"06";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;