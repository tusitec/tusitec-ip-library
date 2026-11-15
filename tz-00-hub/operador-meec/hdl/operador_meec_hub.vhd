library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all; -- O nosso contrato de barramento

entity operador_meec_hub is
    generic (
        G_NUM_SATELLITES : integer := 4 -- Ex: 4 portas de entrada T-Link no Hub
    );
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. As Portas de Entrada (Recebem dados dos IPs Satélites)
        sat_in      : in  t_tlink_s2m_array(0 to G_NUM_SATELLITES-1);
        sat_ready   : out t_tlink_m2s_array(0 to G_NUM_SATELLITES-1);
        
        -- 2. A Porta de Saída Master (O dado já purificado pelo MEEC)
        m_out       : out t_tlink_s2m;
        m_ready     : in  t_tlink_m2s
    );
end entity;

architecture rtl of operador_meec_hub is
    -- Registrador para saber qual canal estamos atendendo agora
    signal current_channel : integer range 0 to G_NUM_SATELLITES-1;
    
    -- Sinais internos para a Máquina de Matemática do MEEC
    signal meec_core_data_in  : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal meec_core_data_out : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal meec_core_valid    : std_logic;
begin

    -------------------------------------------------------------------
    -- 1. O ÁRBITRO ROUND-ROBIN (Controle de Tráfego)
    -------------------------------------------------------------------
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            current_channel <= 0;
            -- Zera todos os sinais de "Pronto para receber"
            for i in 0 to G_NUM_SATELLITES-1 loop
                sat_ready(i).ready <= '0';
            end loop;
            
        elsif rising_edge(clk) then
            -- Por padrão, o Hub diz a todos os satélites para esperarem
            for i in 0 to G_NUM_SATELLITES-1 loop
                sat_ready(i).ready <= '0';
            end loop;

            -- Verifica se a saída externa está livre para receber (Backpressure)
            if m_ready.ready = '1' then
                
                -- Se o canal atual tem um dado válido, nós o capturamos
                if sat_in(current_channel).valid = '1' then
                    -- 1. Dizemos ao satélite: "Recebi seu dado!"
                    sat_ready(current_channel).ready <= '1';
                    
                    -- 2. Jogamos o dado para a matemática do MEEC
                    meec_core_data_in <= sat_in(current_channel).data;
                    meec_core_valid   <= '1';
                    
                    -- 3. Passa a vez para o próximo satélite de forma justa
                    if current_channel = G_NUM_SATELLITES-1 then
                        current_channel <= 0;
                    else
                        current_channel <= current_channel + 1;
                    end if;
                else
                    -- Se o canal atual está vazio, pula pro próximo imediatamente
                    meec_core_valid <= '0';
                    if current_channel = G_NUM_SATELLITES-1 then
                        current_channel <= 0;
                    else
                        current_channel <= current_channel + 1;
                    end if;
                end if;
            else
                meec_core_valid <= '0'; -- Congela o processamento
            end if;
        end if;
    end process;

    -------------------------------------------------------------------
    -- 2. A MAGIA MATEMÁTICA (O Núcleo de Redução Zonotópica M*)
    -------------------------------------------------------------------
    -- Aqui entra a sua equação MEEC real! 
    -- Para fins de roteamento, faremos um bypass provisório.
    
    meec_core_data_out <= meec_core_data_in; -- Substituir pela lógica MEEC real

    -------------------------------------------------------------------
    -- 3. O DESPACHANTE DE SAÍDA (Roteamento Final)
    -------------------------------------------------------------------
    m_out.valid   <= meec_core_valid;
    m_out.data    <= meec_core_data_out;
    m_out.channel <= std_logic_vector(to_unsigned(current_channel, C_TLINK_CH_WIDTH));
    m_out.sop     <= sat_in(current_channel).sop;
    m_out.eop     <= sat_in(current_channel).eop;

end architecture rtl;