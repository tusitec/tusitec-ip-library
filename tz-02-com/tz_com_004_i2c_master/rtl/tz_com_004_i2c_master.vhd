library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_com_004_i2c_master is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sda : inout std_logic;
        scl : inout std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_com_004_i2c_master is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            sda <= 'Z'; scl <= 'Z';
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            if din(0) = '0' then sda <= '0'; else sda <= 'Z'; end if;
        if din(1) = '0' then scl <= '0'; else scl <= 'Z'; end if;
        int_data(0) <= sda; int_data(1) <= scl;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"0E";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
