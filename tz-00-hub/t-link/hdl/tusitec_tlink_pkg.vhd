library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package tusitec_tlink_pkg is

    -- =========================================================
    -- TUSITEC T-LINK PROTOCOL - CONFIGURAÇÕES GLOBAIS
    -- =========================================================
    constant C_TLINK_DATA_WIDTH : integer := 32;
    constant C_TLINK_CH_WIDTH   : integer := 8;

    -- =========================================================
    -- RECORD 1: Satélite para Master (Sentido TX)
    -- =========================================================
    type t_tlink_s2m is record
        valid   : std_logic;
        data    : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        channel : std_logic_vector(C_TLINK_CH_WIDTH-1 downto 0);
        sop     : std_logic;
        eop     : std_logic;
    end record;

    -- =========================================================
    -- RECORD 2: Master para Satélite (Sentido RX - Backpressure)
    -- =========================================================
    type t_tlink_m2s is record
        ready   : std_logic;
    end record;

    -- =========================================================
    -- ARRAYS DE MÚLTIPLAS ROTAS (Correção para o Operador MEEC)
    -- =========================================================
    -- Permite que o Hub instancie portas como: port(sat_in : in t_tlink_s2m_array(0 to 3))
    type t_tlink_s2m_array is array (natural range <>) of t_tlink_s2m;
    type t_tlink_m2s_array is array (natural range <>) of t_tlink_m2s;

end package tusitec_tlink_pkg;