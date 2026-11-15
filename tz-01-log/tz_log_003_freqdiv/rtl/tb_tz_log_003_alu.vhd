library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_log_003_alu is
end entity;

architecture sim of tb_tz_log_003_alu is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    
    signal opcode   : std_logic_vector(1 downto 0) := "00";
    signal din_a    : std_logic_vector(31 downto 0) := (others => '0');
    signal din_b    : std_logic_vector(31 downto 0) := (others => '0');
    
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    dut: entity work.tz_log_003_alu
        port map (
            clk      => clk,
            rst_n    => rst_n,
            opcode   => opcode,
            din_a    => din_a,
            din_b    => din_b,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    stim_proc: process
    begin
        rst_n <= '0';
        tlink_rx.ready <= '0';
        wait for 20 ns;
        rst_n <= '1';
        wait for 20 ns;
        
        tlink_rx.ready <= '1';
        
        -- Injeta dados numéricos nas portas A e B (Ex: 10 e 5)
        din_a <= x"0000_000A"; -- Decimal 10
        din_b <= x"0000_0005"; -- Decimal 5
        
        -- Testa SOMA (Espera 15 na saída T-Link)
        opcode <= "00";
        wait for 30 ns;
        
        -- Testa SUBTRAÇÃO (Espera 5 na saída T-Link)
        opcode <= "01";
        wait for 30 ns;
        
        -- Testa AND Lógico
        opcode <= "10";
        wait for 30 ns;
        
        wait;
    end process;
end architecture sim;