library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_003_freqdiv is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        divisor     : in  std_logic_vector(31 downto 0); -- Fator de divisão
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_003_freqdiv is
    signal counter    : unsigned(31 downto 0);
    signal tick       : std_logic;
begin
    -------------------------------------------------------------------
    -- 1. LÓGICA CORE: Divisor de Frequência
    -------------------------------------------------------------------
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            counter <= (others => '0');
            tick    <= '0';
        elsif rising_edge(clk) then
            if counter >= unsigned(divisor) - 1 then
                counter <= (others => '0');
                tick    <= '1';
            else
                counter <= counter + 1;
                tick    <= '0';
            end if;
        end if;
    end process;

    -------------------------------------------------------------------
    -- 2. ENCAPSULAMENTO T-LINK
    -------------------------------------------------------------------
    tlink_tx.valid   <= tick; -- Só levanta a flag quando o divisor zera
    tlink_tx.data    <= std_logic_vector(to_unsigned(1, C_TLINK_DATA_WIDTH)); -- Envia '1' como sinal de pulso
    tlink_tx.channel <= x"03"; -- ID: TZ-LOG-003
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;