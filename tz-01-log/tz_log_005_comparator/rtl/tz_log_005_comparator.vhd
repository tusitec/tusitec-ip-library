library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_005_comparator is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- INTERFACE FISICA DO IP
        din_a : in std_logic_vector(31 downto 0);
        din_b : in std_logic_vector(31 downto 0);
        eq_out : out std_logic;
        gt_out : out std_logic;
        lt_out : out std_logic;
        
        -- INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_005_comparator is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
    
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            internal_data <= (others => '0');
            
        elsif rising_edge(clk) then
            internal_data <= (others => '0'); 
            if unsigned(din_a) = unsigned(din_b) then eq_out <= '1'; internal_data(0) <= '1'; else eq_out <= '0'; internal_data(0) <= '0'; end if;
        if unsigned(din_a) > unsigned(din_b) then gt_out <= '1'; internal_data(1) <= '1'; else gt_out <= '0'; internal_data(1) <= '0'; end if;
        if unsigned(din_a) < unsigned(din_b) then lt_out <= '1'; internal_data(2) <= '1'; else lt_out <= '0'; internal_data(2) <= '0'; end if;
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
    tlink_tx.channel <= x"05"; 
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
