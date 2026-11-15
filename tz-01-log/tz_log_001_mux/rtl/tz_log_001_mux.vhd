library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all; -- Herda o contrato de comunicação

entity tz_log_001_mux is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- ==========================================
        -- 1. INTERFACE ESPECÍFICA DO IP (Mux/Demux)
        -- ==========================================
        sel         : in  std_logic; -- Pino de seleção do multiplexador
        din_0       : in  std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        din_1       : in  std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        
        -- ==========================================
        -- 2. INTERFACE T-LINK (Rumo ao Operador MEEC)
        -- ==========================================
        tlink_tx    : out t_tlink_s2m; -- Transmite para o sat_in do Hub
        tlink_rx    : in  t_tlink_m2s  -- Recebe o sat_ready do Hub
    );
end entity;

architecture rtl of tz_log_001_mux is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
begin
    -------------------------------------------------------------------
    -- 1. LÓGICA CORE DO IP (Multiplexador Digital)
    -------------------------------------------------------------------
    -- Aqui entra a finalidade real do IP Core (Seleção de sinais)
    process(sel, din_0, din_1)
    begin
        if sel = '0' then
            internal_data <= din_0;
        else
            internal_data <= din_1;
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
            -- O IP sinaliza que tem um dado processado e válido
            valid_flag <= '1'; 
            
            -- Se o Hub respondeu com 'ready', o IP sabe que o dado foi engolido
            if tlink_rx.ready = '1' then
                -- Lógica de backpressure: aguarda novo ciclo ou novo dado
            end if;
        end if;
    end process;

    -------------------------------------------------------------------
    -- 3. EMPACOTAMENTO DA SAÍDA
    -------------------------------------------------------------------
    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= internal_data;
    tlink_tx.channel <= x"01"; -- ID Único deste Satélite
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';

end architecture rtl;