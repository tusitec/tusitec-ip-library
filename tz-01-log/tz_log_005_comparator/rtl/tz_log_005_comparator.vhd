library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_005_comparator is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        data_a      : in  std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        data_b      : in  std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        compare_en  : in  std_logic;
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_005_comparator is
    signal result_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag  : std_logic;
begin
    -------------------------------------------------------------------
    -- 1. LÓGICA CORE: Comparador Digital Zero-DSP
    -------------------------------------------------------------------
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            result_data <= (others => '0');
            valid_flag  <= '0';
        elsif rising_edge(clk) then
            if compare_en = '1' then
                valid_flag <= '1';
                if signed(data_a) > signed(data_b) then
                    result_data <= std_logic_vector(to_signed(1, C_TLINK_DATA_WIDTH));  -- A > B
                elsif signed(data_a) < signed(data_b) then
                    result_data <= std_logic_vector(to_signed(-1, C_TLINK_DATA_WIDTH)); -- A < B
                else
                    result_data <= (others => '0');                                     -- A = B
                end if;
            else
                valid_flag <= '0';
            end if;
        end if;
    end process;

    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= result_data;
    tlink_tx.channel <= x"05"; -- ID: TZ-LOG-005
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;