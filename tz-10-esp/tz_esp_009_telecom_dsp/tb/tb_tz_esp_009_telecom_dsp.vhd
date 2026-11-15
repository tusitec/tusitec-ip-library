library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_esp_009_telecom_dsp is
end entity;

architecture sim of tb_tz_esp_009_telecom_dsp is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal iq_in : std_logic_vector(31 downto 0) := (others => '0');
    signal sym_out : std_logic_vector(15 downto 0);
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_esp_009_telecom_dsp
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, iq_in => iq_in, sym_out => sym_out,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        iq_in <= x"0F0F00FF"; wait for 50 ns;
        wait;
    end process;
end architecture sim;
