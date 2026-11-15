library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_004_async_fifo is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        rd_clk : in std_logic;
        wr_en : in std_logic;
        rd_en : in std_logic;
        dout : out std_logic_vector(31 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_004_async_fifo is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    type fifo_type is array (0 to 15) of std_logic_vector(31 downto 0);
    signal fifo_mem : fifo_type := (others => (others => '0'));
    signal wr_ptr, rd_ptr : unsigned(3 downto 0) := (others => '0');
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            wr_ptr <= (others => '0'); dout <= (others => '0');
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            if wr_en = '1' then fifo_mem(to_integer(wr_ptr)) <= din; wr_ptr <= wr_ptr + 1; end if;
        if rd_en = '1' then dout <= fifo_mem(to_integer(rd_ptr)); rd_ptr <= rd_ptr + 1; else dout <= (others => '0'); end if;
        int_data(3 downto 0) <= std_logic_vector(wr_ptr);
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"40";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
