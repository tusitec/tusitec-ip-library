library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_dsp_010_demodulator is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        mod_in : in std_logic_vector(15 downto 0);
        carrier_ref : in std_logic_vector(15 downto 0);
        msg_out : out std_logic_vector(15 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_dsp_010_demodulator is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    signal mult : unsigned(31 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            msg_out <= (others => '0'); mult <= (others => '0');
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            mult <= unsigned(mod_in) * unsigned(carrier_ref);
        msg_out <= std_logic_vector(mult(31 downto 16));
        int_data(15 downto 0) <= std_logic_vector(mult(31 downto 16));
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"3C";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
