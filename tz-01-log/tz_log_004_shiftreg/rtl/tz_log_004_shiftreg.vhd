library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_004_shiftreg is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        serial_in   : in  std_logic;
        shift_en    : in  std_logic;
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_004_shiftreg is
    signal shift_reg   : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal bit_counter : integer range 0 to C_TLINK_DATA_WIDTH := 0;
    signal valid_flag  : std_logic;
begin
    -------------------------------------------------------------------
    -- 1. LÓGICA CORE: Registrador de Deslocamento
    -------------------------------------------------------------------
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            shift_reg   <= (others => '0');
            bit_counter <= 0;
            valid_flag  <= '0';
        elsif rising_edge(clk) then
            -- Default: não envia dado até encher
            valid_flag <= '0'; 
            
            if shift_en = '1' then
                -- Desloca para a esquerda e injeta o novo bit no LSB
                shift_reg <= shift_reg(C_TLINK_DATA_WIDTH-2 downto 0) & serial_in;
                
                if bit_counter = C_TLINK_DATA_WIDTH - 1 then
                    bit_counter <= 0;
                    valid_flag  <= '1'; -- Dispara a transmissão no T-Link
                else
                    bit_counter <= bit_counter + 1;
                end if;
            end if;
        end if;
    end process;

    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= shift_reg;
    tlink_tx.channel <= x"04"; -- ID: TZ-LOG-004
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;