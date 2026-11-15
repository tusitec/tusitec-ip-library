library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_sys_003_int_ctrl is
end entity;

architecture sim of tb_tz_sys_003_int_ctrl is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal irq_lines : std_logic_vector(7 downto 0) := (others => '0');
    signal irq_req : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_sys_003_int_ctrl
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, irq_lines => irq_lines, irq_req => irq_req,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din(7 downto 0) <= x"FF"; irq_lines <= x"01"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
