library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_tz_sys_009_soc_interconnect is
end entity;

architecture sim of tb_tz_sys_009_soc_interconnect is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    signal din : std_logic_vector(31 downto 0) := (others => '0');
    signal m0_req, s0_ack : std_logic := '0';
    signal m0_grant : std_logic;
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.tz_sys_009_soc_interconnect
        port map (
            clk      => clk,
            rst_n    => rst_n,
            din => din, m0_req => m0_req, s0_ack => s0_ack, m0_grant => m0_grant,
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        m0_req <= '1'; s0_ack <= '1'; wait for 50 ns;
        wait;
    end process;
end architecture sim;
