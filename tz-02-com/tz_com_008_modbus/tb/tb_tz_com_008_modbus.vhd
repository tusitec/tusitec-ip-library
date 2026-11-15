library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_com_008_modbus is
end entity;

architecture sim of tb_tz_com_008_modbus is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal rs485_tx, rs485_en : std_logic;
    signal rs485_rx : std_logic := '1';
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_com_008_modbus
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, rs485_tx => rs485_tx, rs485_rx => rs485_rx, rs485_en => rs485_en,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        rs485_rx <= '0'; wait for 20 ns; rs485_rx <= '1';
        wait;
    end process;
end architecture sim;
