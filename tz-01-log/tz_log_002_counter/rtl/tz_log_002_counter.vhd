library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_002_counter is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        enable      : in  std_logic;
        clear       : in  std_logic;
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_002_counter is
    signal reg_count  : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag : std_logic;
begin
    -------------------------------------------------------------------
    -- 1. LÓGICA CORE: Contador Binário
    -------------------------------------------------------------------
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            reg_count <= (others => '0');
        elsif rising_edge(clk) then
            if clear = '1' then
                reg_count <= (others => '0');
            elsif enable = '1' then
                reg_count <= reg_count + 1;
            end if;
        end if;
    end process;

    -------------------------------------------------------------------
    -- 2. MÁQUINA DE ESTADO DO BARRAMENTO T-LINK
    -------------------------------------------------------------------
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            valid_flag <= '0';
        elsif rising_edge(clk) then
            -- O contador está sempre pronto para reportar seu valor
            valid_flag <= '1'; 
        end if;
    end process;

    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= std_logic_vector(reg_count);
    tlink_tx.channel <= x"02"; -- ID: TZ-LOG-002
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;