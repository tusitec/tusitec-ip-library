library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_log_001_mux is
end entity;

architecture sim of tb_tz_log_001_mux is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    
    signal sel      : std_logic := '0';
    signal din_0    : std_logic_vector(31 downto 0) := (others => '0');
    signal din_1    : std_logic_vector(31 downto 0) := (others => '0');
    
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    -- Geração de Clock (100 MHz)
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    -- Instância do TZ-LOG-001
    dut: entity work.tz_log_001_mux
        port map (
            clk      => clk,
            rst_n    => rst_n,
            sel      => sel,
            din_0    => din_0,
            din_1    => din_1,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    -- Sequência de Teste
    stim_proc: process
    begin
        -- Reset
        rst_n <= '0';
        tlink_rx.ready <= '0'; -- Simula o Hub ocupado
        wait for 20 ns;
        rst_n <= '1';
        
        -- Injeta dados brutos no IP
        din_0 <= x"AAAA_0000";
        din_1 <= x"BBBB_1111";
        
        -- Seleciona Canal 0
        sel <= '0';
        wait for 20 ns;
        
        -- Simula o Hub engolindo o dado
        tlink_rx.ready <= '1';
        wait for 10 ns;
        tlink_rx.ready <= '0';
        
        -- Seleciona Canal 1
        sel <= '1';
        wait for 20 ns;
        
        wait;
    end process;
end architecture sim;