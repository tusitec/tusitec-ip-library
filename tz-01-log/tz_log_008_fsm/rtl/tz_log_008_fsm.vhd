library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_008_fsm is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        trigger     : in  std_logic;
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_008_fsm is
    type t_state is (ST_IDLE, ST_RUN, ST_DONE);
    signal current_state, next_state : t_state;
    signal state_code : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
begin
    -- Registro de Estado
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            current_state <= ST_IDLE;
        elsif rising_edge(clk) then
            current_state <= next_state;
        end if;
    end process;

    -- Lógica Combinacional de Transição
    process(current_state, trigger)
    begin
        next_state <= current_state;
        case current_state is
            when ST_IDLE =>
                if trigger = '1' then next_state <= ST_RUN; end if;
            when ST_RUN =>
                next_state <= ST_DONE; -- Lógica fictícia para preencher futuramente
            when ST_DONE =>
                next_state <= ST_IDLE;
        end case;
    end process;

    -- Decodificação de Estado para o T-Link
    process(current_state)
    begin
        case current_state is
            when ST_IDLE => state_code <= x"0000_0000";
            when ST_RUN  => state_code <= x"0000_0001";
            when ST_DONE => state_code <= x"0000_0002";
        end case;
    end process;

    tlink_tx.valid   <= '1'; -- Reporta o estado continuamente
    tlink_tx.data    <= state_code;
    tlink_tx.channel <= x"08";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;