library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_sys_004_int_bus is
end entity;

architecture sim of tb_tz_sys_004_int_bus is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    
    -- Sinais do Barramento T-Link
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    -- Geracao de Clock (100 MHz)
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    -- Instancia do DUT (Device Under Test)
    dut: entity work.tz_sys_004_int_bus
        port map (
            clk      => clk,
            rst_n    => rst_n,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    -- Sequencia de Teste de Base
    stim_proc: process
    begin
        -- Reset da interface
        rst_n <= '0';
        tlink_rx.ready <= '0'; -- Hub ocupado
        wait for 20 ns;
        rst_n <= '1';
        wait for 20 ns;
        
        -- Hub livre para receber dados
        tlink_rx.ready <= '1';
        wait for 50 ns;
        
        -- TODO: Inserir injeção de estimulos especificos do IP aqui
        
        wait;
    end process;
end architecture sim;
