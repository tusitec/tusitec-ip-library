library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_vid_008_shape_gen is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- ==========================================
        -- 1. INTERFACE ESPECIFICA DO IP (Geometric Shape Generator)
        -- ==========================================
        -- TODO: Declarar os pinos fisicos e de controle especificos aqui
        
        -- ==========================================
        -- 2. INTERFACE T-LINK (Rumo ao Operador MEEC)
        -- ==========================================
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_vid_008_shape_gen is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
begin
    -------------------------------------------------------------------
    -- 1. LOGICA CORE DO IP (Geometric Shape Generator)
    -------------------------------------------------------------------
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            internal_data <= (others => '0');
        elsif rising_edge(clk) then
            -- TODO: Inserir a logica especifica do componente VHDL
            internal_data <= (others => '0'); -- Placeholder
        end if;
    end process;

    -------------------------------------------------------------------
    -- 2. MAQUINA DE ESTADO DO BARRAMENTO T-LINK
    -------------------------------------------------------------------
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            valid_flag <= '0';
        elsif rising_edge(clk) then
            -- TODO: Levantar flag para '1' quando o processamento concluir
            valid_flag <= '0'; -- Placeholder
        end if;
    end process;

    -------------------------------------------------------------------
    -- 3. EMPACOTAMENTO DA SAIDA
    -------------------------------------------------------------------
    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= internal_data;
    tlink_tx.channel <= x"30"; -- ID Unico do Satelite
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';

end architecture rtl;
