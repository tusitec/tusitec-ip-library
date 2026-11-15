library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_com_003_spi_slave is
end entity;

architecture sim of tb_tz_com_003_spi_slave is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal mosi, sck : std_logic := '0';
    signal cs_n : std_logic := '1';
    signal miso : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_com_003_spi_slave
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, mosi => mosi, miso => miso, sck => sck, cs_n => cs_n,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        cs_n <= '0'; mosi <= '1'; wait for 10 ns; sck <= '1'; wait for 10 ns; sck <= '0'; cs_n <= '1';
        wait;
    end process;
end architecture sim;
