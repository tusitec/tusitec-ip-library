library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_002_rom is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        addr : in std_logic_vector(9 downto 0);
        dout : out std_logic_vector(31 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_002_rom is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    type rom_type is array (0 to 3) of std_logic_vector(31 downto 0);
    constant rom_block : rom_type := (
        x"0000_0001", x"0000_0002", x"0000_0003", x"0000_0004"
    );
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
            if to_integer(unsigned(addr)) < 4 then data_out_reg <= rom_block(to_integer(unsigned(addr))); else data_out_reg <= (others => '0'); end if;
        dout <= data_out_reg;
        int_data <= data_out_reg;
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"3E";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
