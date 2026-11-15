library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_operador_meec_hub is
end entity;

architecture sim of tb_operador_meec_hub is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    
    signal m_rx : t_tlink_m2s;
    signal m_tx : t_tlink_s2m;
    
    signal s0_din, s1_din, s2_din, s3_din : std_logic_vector(31 downto 0);
    signal s0_tx, s1_tx, s2_tx, s3_tx : t_tlink_s2m := ('0', (others => '0'), (others => '0'), '0', '0');
    signal s0_rx, s1_rx, s2_rx, s3_rx : t_tlink_m2s;
    
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.operador_meec_hub
        generic map (
            CH_SAT0 => x"0B", CH_SAT1 => x"15", CH_SAT2 => x"33", CH_SAT3 => x"3D"
        )
        port map (
            clk => clk, rst_n => rst_n,
            m_tlink_rx => m_rx, m_tlink_tx => m_tx,
            sat0_din => s0_din, sat0_tx => s0_tx, sat0_rx => s0_rx,
            sat1_din => s1_din, sat1_tx => s1_tx, sat1_rx => s1_rx,
            sat2_din => s2_din, sat2_tx => s2_tx, sat2_rx => s2_rx,
            sat3_din => s3_din, sat3_tx => s3_tx, sat3_rx => s3_rx
        );

    process
    begin
        rst_n <= '0'; 
        m_rx.valid <= '0'; m_rx.data <= (others => '0'); m_rx.channel <= (others => '0');
        wait for 20 ns;
        
        rst_n <= '1'; 
        wait for 20 ns;
        
        -- Teste: O Mestre (Operador M*) quer falar com o PWM (Canal x15)
        m_rx.valid <= '1';
        m_rx.channel <= x"15";
        m_rx.data <= x"DEADBEEF";
        wait for 10 ns;
        m_rx.valid <= '0';
        wait for 40 ns;
        
        -- Teste: A RAM (Satelite 3, Canal x3D) envia um dado de volta ao Mestre
        s3_tx.valid <= '1';
        s3_tx.channel <= x"3D";
        s3_tx.data <= x"CAFEBABE";
        wait for 10 ns;
        s3_tx.valid <= '0';
        
        wait;
    end process;
end architecture sim;
