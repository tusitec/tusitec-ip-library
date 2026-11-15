library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_001_ram is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        addr : in std_logic_vector(9 downto 0);
        we : in std_logic;
        dout : out std_logic_vector(31 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_001_ram is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    type ram_type is array (0 to 1023) of std_logic_vector(31 downto 0);
    signal ram_block : ram_type := (others => (others => '0'));
    signal data_out_reg : std_logic_vector(31 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            data_out_reg <= (others => '0'); dout <= (others => '0');
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            if we = '1' then ram_block(to_integer(unsigned(addr))) <= din; end if;
        data_out_reg <= ram_block(to_integer(unsigned(addr)));
        dout <= data_out_reg;
        int_data <= data_out_reg;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"3D";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
