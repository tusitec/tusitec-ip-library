library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_operador_meec_hub is
    -- Testbenches não possuem portas de entrada/saída reais
end entity;

architecture sim of tb_operador_meec_hub is

    -- =========================================================
    -- 1. SINAIS DE CONTROLE E CLOCK
    -- =========================================================
    signal clk   : std_logic := '0';
    signal rst_n : std_logic := '0';
    constant CLK_PERIOD : time := 10 ns; -- Simulando FPGA a 100 MHz

    -- =========================================================
    -- 2. SINAIS DO BARRAMENTO T-LINK
    -- =========================================================
    -- Array de 4 satélites (0 a 3) inicializado em zero para evitar "U" (Uninitialized)
    signal sat_in        : t_tlink_s2m_array(0 to 3) := (others => (valid => '0', data => (others => '0'), channel => (others => '0'), sop => '0', eop => '0'));
    signal sat_ready_out : t_tlink_m2s_array(0 to 3);
    
    -- Saída Mestre (O que vai para a Ponte AXI4 ou Processador)
    signal m_out         : t_tlink_s2m;
    signal m_ready_in    : t_tlink_m2s := (ready => '0');

begin

    -- =========================================================
    -- 3. INSTÂNCIA DO NOSSO NÚCLEO (Device Under Test)
    -- =========================================================
    dut : entity work.operador_meec_hub
        port map (
            clk             => clk,
            rst_n           => rst_n,
            sat_in          => sat_in,
            sat_ready_out   => sat_ready_out,
            m_out           => m_out,
            m_ready_in      => m_ready_in
        );

    -- =========================================================
    -- 4. GERADOR DE CLOCK (Batimento Cardíaco do FPGA)
    -- =========================================================
    clk_process : process
    begin
        clk <= '0';
        wait for CLK_PERIOD / 2;
        clk <= '1';
        wait for CLK_PERIOD / 2;
    end process;

    -- =========================================================
    -- 5. INJEÇÃO DE ESTÍMULOS (Testando a Física)
    -- =========================================================
    stim_process : process
    begin
        -- A. Reset Inicial (Hardware limpo)
        rst_n <= '0';
        wait for 20 ns;
        rst_n <= '1';
        wait for 20 ns;

        -- B. Destino Pronto (O receptor avisa ao Hub que tem espaço na RAM)
        m_ready_in.ready <= '1';
        wait for CLK_PERIOD;

        -- C. O TESTE DE COLISÃO (Stress Test)
        -- Satélite 0 (Fusão de Sensores) e Satélite 1 (Visão) 
        -- disparam dados EXATAMENTE no mesmo ciclo de clock.
        
        -- Injeção do Sensor 0
        sat_in(0).valid   <= '1';
        sat_in(0).data    <= x"AAAA_0001"; -- Dado Falso de Giroscópio
        sat_in(0).channel <= x"00";
        sat_in(0).sop     <= '1';
        
        -- Injeção da Câmera 1
        sat_in(1).valid   <= '1';
        sat_in(1).data    <= x"BBBB_0002"; -- Dado Falso de Pixel
        sat_in(1).channel <= x"01";
        sat_in(1).sop     <= '1';
        
        wait for CLK_PERIOD;

        -- Remove o bit de Start of Packet (SOP)
        sat_in(0).sop <= '0';
        sat_in(1).sop <= '0';

        -- Deixa o Árbitro trabalhar por 5 ciclos para vermos quem ele atendeu primeiro
        wait for CLK_PERIOD * 5;

        -- D. Desliga os satélites (Fim de Pacote)
        sat_in(0).eop <= '1';
        sat_in(1).eop <= '1';
        wait for CLK_PERIOD;
        
        sat_in(0).valid <= '0';
        sat_in(1).valid <= '0';
        sat_in(0).eop   <= '0';
        sat_in(1).eop   <= '0';

        -- Encerra a simulação congelando a thread
        wait;
    end process;

end architecture sim;