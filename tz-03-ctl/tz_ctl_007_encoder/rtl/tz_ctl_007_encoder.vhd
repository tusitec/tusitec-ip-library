library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_ctl_007_encoder is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        enc_a : in std_logic;
        enc_b : in std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_ctl_007_encoder is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    signal a_d : std_logic;
    signal count : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            a_d <= '0'; count <= (others => '0');
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            a_d <= enc_a;
        if enc_a = '1' and a_d = '0' then
            if enc_b = '1' then count <= count + 1; else count <= count - 1; end if;
        end if;
        int_data <= std_logic_vector(count);
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"1B";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
