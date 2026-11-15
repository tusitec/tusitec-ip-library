library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_003_freqdiv is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- INTERFACE FISICA DO IP
        div_factor : in std_logic_vector(31 downto 0);
        clk_out : out std_logic;
        
        -- INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_003_freqdiv is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
    signal count_reg : unsigned(31 downto 0);
    signal clk_out_reg : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            internal_data <= (others => '0');
            count_reg <= (others => '0'); clk_out_reg <= '0';
        elsif rising_edge(clk) then
            internal_data <= (others => '0'); 
            if count_reg >= unsigned(div_factor) then count_reg <= (others => '0'); clk_out_reg <= not clk_out_reg; else count_reg <= count_reg + 1; end if;
        clk_out <= clk_out_reg; internal_data(0) <= clk_out_reg;
        end if;
    end process;

    process(clk, rst_n)
    begin
        if rst_n = '0' then
            valid_flag <= '0';
        elsif rising_edge(clk) then
            valid_flag <= '1';
        end if;
    end process;

    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= internal_data;
    tlink_tx.channel <= x"03"; 
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
