library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tz_log_007_alu is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- 1. INTERFACE ESPECÍFICA DO IP
        opcode      : in  std_logic_vector(2 downto 0);
        data_a      : in  std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        data_b      : in  std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        execute     : in  std_logic;
        
        -- 2. INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of tz_log_007_alu is
    signal alu_result : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            alu_result <= (others => '0');
            valid_flag <= '0';
        elsif rising_edge(clk) then
            valid_flag <= execute;
            if execute = '1' then
                case opcode is
                    when "000" => alu_result <= std_logic_vector(signed(data_a) + signed(data_b));
                    when "001" => alu_result <= std_logic_vector(signed(data_a) - signed(data_b));
                    when "010" => alu_result <= data_a and data_b;
                    when "011" => alu_result <= data_a or data_b;
                    when "100" => alu_result <= data_a xor data_b;
                    when others => alu_result <= (others => '0');
                end case;
            end if;
        end if;
    end process;

    tlink_tx.valid   <= valid_flag;
    tlink_tx.data    <= alu_result;
    tlink_tx.channel <= x"07";
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;