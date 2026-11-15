library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_007_alu is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- INTERFACE FISICA DO IP
        opcode : in std_logic_vector(1 downto 0);
        din_a : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        din_b : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        
        -- INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_007_alu is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
    signal a_uns, b_uns : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            internal_data <= (others => '0');
            
        elsif rising_edge(clk) then
            internal_data <= (others => '0'); 
            a_uns <= unsigned(din_a); b_uns <= unsigned(din_b);
        case opcode is
            when "00" => internal_data <= std_logic_vector(a_uns + b_uns);
            when "01" => internal_data <= std_logic_vector(a_uns - b_uns);
            when "10" => internal_data <= din_a and din_b;
            when "11" => internal_data <= din_a or din_b;
            when others => internal_data <= (others => '0');
        end case;
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
    tlink_tx.channel <= x"07"; 
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
