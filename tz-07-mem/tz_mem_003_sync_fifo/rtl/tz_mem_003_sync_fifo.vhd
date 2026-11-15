library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_003_sync_fifo is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        wr_en : in std_logic;
        rd_en : in std_logic;
        dout : out std_logic_vector(31 downto 0);
        full : out std_logic;
        empty : out std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_003_sync_fifo is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    type fifo_type is array (0 to 15) of std_logic_vector(31 downto 0);
    signal fifo_mem : fifo_type := (others => (others => '0'));
    signal wr_ptr, rd_ptr : unsigned(3 downto 0) := (others => '0');
    signal count : unsigned(4 downto 0) := (others => '0');
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            wr_ptr <= (others => '0'); rd_ptr <= (others => '0'); count <= (others => '0'); dout <= (others => '0'); full <= '0'; empty <= '1';
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            if wr_en = '1' and count < 16 then fifo_mem(to_integer(wr_ptr)) <= din; wr_ptr <= wr_ptr + 1; end if;
        if rd_en = '1' and count > 0 then dout <= fifo_mem(to_integer(rd_ptr)); rd_ptr <= rd_ptr + 1; else dout <= (others => '0'); end if;
        if wr_en = '1' and rd_en = '0' and count < 16 then count <= count + 1;
        elsif wr_en = '0' and rd_en = '1' and count > 0 then count <= count - 1; end if;
        if count = 16 then full <= '1'; else full <= '0'; end if;
        if count = 0 then empty <= '1'; else empty <= '0'; end if;
        int_data(4 downto 0) <= std_logic_vector(count);
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"3F";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
