library ieee;
use ieee.std_logic_1164.all;
use work.tusitec_tlink_pkg.all; -- O nosso pacote T-Link obrigatório

entity tlink_to_axi4_bridge is
    port (
        -- Clocks de Sistema (AXI exige clock, mesmo para lógica puramente combinacional)
        clk             : in  std_logic;
        rst_n           : in  std_logic;
        
        -- =========================================================
        -- LADO 1: A Entrada Tusitec (Conectada à saída do Operador MEEC)
        -- =========================================================
        tlink_in        : in  t_tlink_s2m;
        tlink_ready_out : out t_tlink_m2s;
        
        -- =========================================================
        -- LADO 2: A Saída AXI4-Stream (Vai para o mundo Xilinx/Zynq)
        -- =========================================================
        m_axis_tvalid   : out std_logic;
        m_axis_tready   : in  std_logic;
        m_axis_tdata    : out std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        m_axis_tlast    : out std_logic;
        m_axis_tid      : out std_logic_vector(C_TLINK_CH_WIDTH-1 downto 0)
    );
end entity;

architecture rtl of tlink_to_axi4_bridge is
begin

    -- -------------------------------------------------------------------------
    -- TRADUÇÃO DE HARDWARE (ZERO-LATENCY / ZERO-DSP)
    -- -------------------------------------------------------------------------
    -- Na síntese do FPGA, isso aqui não consome NENHUM elemento lógico (LE).
    -- O compilador transforma isso em meras "trilhas de cobre" diretas.
    
    -- 1. Sincronia e Aperto de Mão (Handshake)
    m_axis_tvalid         <= tlink_in.valid;
    tlink_ready_out.ready <= m_axis_tready;
    
    -- 2. Os Dados Brutos
    m_axis_tdata          <= tlink_in.data;
    
    -- 3. Identificador de Rota / Canal
    -- O nosso "Channel" (ex: Canal 01 = Sensores) vira o "Thread ID" (TID) do AXI
    m_axis_tid            <= tlink_in.channel;
    
    -- 4. O Delimitador de Pacote
    -- O AXI4-Stream não usa sinal de "Início" (SOP), apenas o de Fim (TLAST)
    m_axis_tlast          <= tlink_in.eop;

end architecture rtl;