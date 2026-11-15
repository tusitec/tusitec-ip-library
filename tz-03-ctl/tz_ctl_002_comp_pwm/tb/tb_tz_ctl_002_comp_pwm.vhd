library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_ctl_002_comp_pwm is
end entity;

architecture sim of tb_tz_ctl_002_comp_pwm is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal pwm_h, pwm_l : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_ctl_002_comp_pwm
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, pwm_h => pwm_h, pwm_l => pwm_l,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        din <= x"0000_000A"; wait for 100 ns;
        wait;
    end process;
end architecture sim;
