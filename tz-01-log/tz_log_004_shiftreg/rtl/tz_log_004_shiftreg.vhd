library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_004_shiftreg is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- INTERFACE FISICA DO IP
        shift_en : in std_logic;
        ser_in : in std_logic;
        par_out : out std_logic_vector(31 downto 0);
        
        -- INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_004_shiftreg is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
    signal shift_reg : std_logic_vector(31 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            internal_data <= (others => '0');
            shift_reg <= (others => '0');
        elsif rising_edge(clk) then
            internal_data <= (others => '0'); 
            if shift_en = '1' then shift_reg <= shift_reg(30 downto 0) & ser_in; end if;
        par_out <= shift_reg; internal_data <= shift_reg;
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
    tlink_tx.channel <= x"04"; 
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
