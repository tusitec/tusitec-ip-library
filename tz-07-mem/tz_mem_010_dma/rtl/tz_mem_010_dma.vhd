library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_mem_010_dma is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        req_in : in std_logic;
        ack_out : out std_logic;
        addr_out : out std_logic_vector(31 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_mem_010_dma is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
    signal src_addr, dst_addr : unsigned(31 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            ack_out <= '0'; addr_out <= (others => '0'); src_addr <= (others => '0'); dst_addr <= (others => '0');
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            if din(0) = '1' then src_addr <= unsigned(din); dst_addr <= unsigned(din) + x"1000"; end if;
        if req_in = '1' then ack_out <= '1'; addr_out <= std_logic_vector(src_addr); src_addr <= src_addr + 1; else ack_out <= '0'; end if;
        int_data <= std_logic_vector(dst_addr);
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
    tlink_tx.channel <= x"46";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
