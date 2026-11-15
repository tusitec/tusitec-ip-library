import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-01-log"
    
    # Dicionário de Hardware: Mapeado exatamente para as 10 pastas locais
    ips = {
        "tz_log_001_mux": {
            "ch": "01",
            "ports": "sel : in std_logic;\n        din_a : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        din_b : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0)",
            "signals": "", "reset": "",
            "core": "if sel = '0' then internal_data <= din_a; else internal_data <= din_b; end if;",
            "tbsig": "signal sel : std_logic := '0';\n    signal din_a, din_b : std_logic_vector(31 downto 0) := (others => '0');",
            "tbmap": "sel => sel, din_a => din_a, din_b => din_b,",
            "tbstim": "din_a <= x\"AAAA_0000\"; din_b <= x\"BBBB_1111\"; sel <= '0'; wait for 50 ns; sel <= '1'; wait for 50 ns;"
        },
        "tz_log_002_counter": {
            "ch": "02",
            "ports": "enable : in std_logic;\n        clear : in std_logic",
            "signals": "signal count_reg : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "count_reg <= (others => '0');",
            "core": "if clear = '1' then count_reg <= (others => '0'); elsif enable = '1' then count_reg <= count_reg + 1; end if;\n        internal_data <= std_logic_vector(count_reg);",
            "tbsig": "signal enable, clear : std_logic := '0';",
            "tbmap": "enable => enable, clear => clear,",
            "tbstim": "enable <= '1'; wait for 10 ns; enable <= '0'; wait for 20 ns; clear <= '1'; wait for 10 ns; clear <= '0';"
        },
        "tz_log_003_freqdiv": {
            "ch": "03",
            "ports": "div_factor : in std_logic_vector(31 downto 0);\n        clk_out : out std_logic",
            "signals": "signal count_reg : unsigned(31 downto 0);\n    signal clk_out_reg : std_logic;",
            "reset": "count_reg <= (others => '0'); clk_out_reg <= '0';",
            "core": "if count_reg >= unsigned(div_factor) then count_reg <= (others => '0'); clk_out_reg <= not clk_out_reg; else count_reg <= count_reg + 1; end if;\n        clk_out <= clk_out_reg; internal_data(0) <= clk_out_reg;",
            "tbsig": "signal div_factor : std_logic_vector(31 downto 0) := x\"0000_0005\";\n    signal clk_out : std_logic;",
            "tbmap": "div_factor => div_factor, clk_out => clk_out,",
            "tbstim": "wait for 100 ns;"
        },
        "tz_log_004_shiftreg": {
            "ch": "04",
            "ports": "shift_en : in std_logic;\n        ser_in : in std_logic;\n        par_out : out std_logic_vector(31 downto 0)",
            "signals": "signal shift_reg : std_logic_vector(31 downto 0);",
            "reset": "shift_reg <= (others => '0');",
            "core": "if shift_en = '1' then shift_reg <= shift_reg(30 downto 0) & ser_in; end if;\n        par_out <= shift_reg; internal_data <= shift_reg;",
            "tbsig": "signal shift_en, ser_in : std_logic := '0';\n    signal par_out : std_logic_vector(31 downto 0);",
            "tbmap": "shift_en => shift_en, ser_in => ser_in, par_out => par_out,",
            "tbstim": "ser_in <= '1'; shift_en <= '1'; wait for 10 ns; shift_en <= '0'; wait for 20 ns;"
        },
        "tz_log_005_comparator": {
            "ch": "05",
            "ports": "din_a : in std_logic_vector(31 downto 0);\n        din_b : in std_logic_vector(31 downto 0);\n        eq_out : out std_logic;\n        gt_out : out std_logic;\n        lt_out : out std_logic",
            "signals": "", "reset": "",
            "core": "if unsigned(din_a) = unsigned(din_b) then eq_out <= '1'; internal_data(0) <= '1'; else eq_out <= '0'; internal_data(0) <= '0'; end if;\n        if unsigned(din_a) > unsigned(din_b) then gt_out <= '1'; internal_data(1) <= '1'; else gt_out <= '0'; internal_data(1) <= '0'; end if;\n        if unsigned(din_a) < unsigned(din_b) then lt_out <= '1'; internal_data(2) <= '1'; else lt_out <= '0'; internal_data(2) <= '0'; end if;",
            "tbsig": "signal din_a, din_b : std_logic_vector(31 downto 0) := (others => '0');\n    signal eq_out, gt_out, lt_out : std_logic;",
            "tbmap": "din_a => din_a, din_b => din_b, eq_out => eq_out, gt_out => gt_out, lt_out => lt_out,",
            "tbstim": "din_a <= x\"0000_0010\"; din_b <= x\"0000_0005\"; wait for 30 ns; din_b <= x\"0000_0010\"; wait for 30 ns;"
        },
        "tz_log_006_decoder": {
            "ch": "06",
            "ports": "addr : in std_logic_vector(3 downto 0);\n        dec_out : out std_logic_vector(15 downto 0)",
            "signals": "signal dec_reg : std_logic_vector(15 downto 0);",
            "reset": "dec_reg <= (others => '0');",
            "core": "dec_reg <= (others => '0'); dec_reg(to_integer(unsigned(addr))) <= '1';\n        dec_out <= dec_reg; internal_data(15 downto 0) <= dec_reg;",
            "tbsig": "signal addr : std_logic_vector(3 downto 0) := \"0000\";\n    signal dec_out : std_logic_vector(15 downto 0);",
            "tbmap": "addr => addr, dec_out => dec_out,",
            "tbstim": "addr <= \"0010\"; wait for 30 ns; addr <= \"1111\"; wait for 30 ns;"
        },
        "tz_log_007_alu": {
            "ch": "07",
            "ports": "opcode : in std_logic_vector(1 downto 0);\n        din_a : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        din_b : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0)",
            "signals": "signal a_uns, b_uns : unsigned(C_TLINK_DATA_WIDTH-1 downto 0);",
            "reset": "",
            "core": "a_uns <= unsigned(din_a); b_uns <= unsigned(din_b);\n        case opcode is\n            when \"00\" => internal_data <= std_logic_vector(a_uns + b_uns);\n            when \"01\" => internal_data <= std_logic_vector(a_uns - b_uns);\n            when \"10\" => internal_data <= din_a and din_b;\n            when \"11\" => internal_data <= din_a or din_b;\n            when others => internal_data <= (others => '0');\n        end case;",
            "tbsig": "signal opcode : std_logic_vector(1 downto 0) := \"00\";\n    signal din_a, din_b : std_logic_vector(31 downto 0) := (others => '0');",
            "tbmap": "opcode => opcode, din_a => din_a, din_b => din_b,",
            "tbstim": "din_a <= x\"0000_000A\"; din_b <= x\"0000_0005\"; opcode <= \"00\"; wait for 30 ns; opcode <= \"01\"; wait for 30 ns;"
        },
        "tz_log_008_fsm": {
            "ch": "08",
            "ports": "start : in std_logic;\n        done : out std_logic;\n        state_out : out std_logic_vector(3 downto 0)",
            "signals": "signal state_reg : std_logic_vector(3 downto 0);",
            "reset": "state_reg <= \"0000\";",
            "core": "if start = '1' then state_reg <= \"0001\"; elsif state_reg = \"0001\" then state_reg <= \"0010\"; elsif state_reg = \"0010\" then state_reg <= \"0100\"; else state_reg <= \"0000\"; end if;\n        if state_reg = \"0100\" then done <= '1'; else done <= '0'; end if;\n        state_out <= state_reg; internal_data(3 downto 0) <= state_reg;",
            "tbsig": "signal start : std_logic := '0';\n    signal done : std_logic;\n    signal state_out : std_logic_vector(3 downto 0);",
            "tbmap": "start => start, done => done, state_out => state_out,",
            "tbstim": "start <= '1'; wait for 10 ns; start <= '0'; wait for 50 ns;"
        },
        "tz_log_009_pulsegen": {
            "ch": "09",
            "ports": "trigger : in std_logic;\n        pulse_ticks : in std_logic_vector(15 downto 0);\n        pulse_out : out std_logic",
            "signals": "signal counter : unsigned(15 downto 0);\n    signal active : std_logic;",
            "reset": "counter <= (others => '0'); active <= '0';",
            "core": "if trigger = '1' and active = '0' then active <= '1'; counter <= unsigned(pulse_ticks); elsif active = '1' then if counter = 0 then active <= '0'; else counter <= counter - 1; end if; end if;\n        pulse_out <= active; internal_data(0) <= active;",
            "tbsig": "signal trigger : std_logic := '0';\n    signal pulse_ticks : std_logic_vector(15 downto 0) := x\"0005\";\n    signal pulse_out : std_logic;",
            "tbmap": "trigger => trigger, pulse_ticks => pulse_ticks, pulse_out => pulse_out,",
            "tbstim": "trigger <= '1'; wait for 10 ns; trigger <= '0'; wait for 100 ns;"
        },
        "tz_log_010_widthconv": {
            "ch": "0A",
            "ports": "din_8bit : in std_logic_vector(7 downto 0);\n        dout_32bit : out std_logic_vector(31 downto 0)",
            "signals": "signal extended : std_logic_vector(31 downto 0);",
            "reset": "extended <= (others => '0');",
            "core": "extended(7 downto 0) <= din_8bit; extended(31 downto 8) <= (others => '0');\n        dout_32bit <= extended; internal_data <= extended;",
            "tbsig": "signal din_8bit : std_logic_vector(7 downto 0) := x\"AA\";\n    signal dout_32bit : std_logic_vector(31 downto 0);",
            "tbmap": "din_8bit => din_8bit, dout_32bit => dout_32bit,",
            "tbstim": "din_8bit <= x\"FF\"; wait for 30 ns; din_8bit <= x\"12\"; wait for 30 ns;"
        }
    }

    rtl_tpl = '''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity {ip} is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- INTERFACE FISICA DO IP
        {ports};
        
        -- INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;

architecture rtl of {ip} is
    signal internal_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal valid_flag    : std_logic;
    {signals}
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            internal_data <= (others => '0');
            {reset}
        elsif rising_edge(clk) then
            internal_data <= (others => '0'); 
            {core}
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
    tlink_tx.channel <= x"{ch}"; 
    tlink_tx.sop     <= '0';
    tlink_tx.eop     <= '0';
end architecture rtl;
'''

    tb_tpl = '''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_{ip} is
end entity;

architecture sim of tb_{ip} is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    {tbsig}
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    clk_process: process
    begin
        clk <= '0'; wait for 5 ns;
        clk <= '1'; wait for 5 ns;
    end process;

    dut: entity work.{ip}
        port map (
            clk      => clk,
            rst_n    => rst_n,
            {tbmap}
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    stim_proc: process
    begin
        rst_n <= '0';
        tlink_rx.ready <= '0';
        wait for 20 ns;
        rst_n <= '1';
        wait for 20 ns;
        tlink_rx.ready <= '1';
        
        {tbstim}
        
        wait;
    end process;
end architecture sim;
'''

    print("Iniciando Injecao de Logica na Familia TZ-01-LOG...")
    
    for ip, data in ips.items():
        ip_path = os.path.join(base_dir, ip)
        if not os.path.exists(ip_path): 
            print(f" -> IGNORADO: A pasta {ip} nao foi encontrada (verifique o nome exato).")
            continue
            
        rtl_code = rtl_tpl.replace("{ip}", ip).replace("{ports}", data["ports"]).replace("{reset}", data["reset"]).replace("{core}", data["core"]).replace("{ch}", data["ch"]).replace("{signals}", data["signals"])
        with open(os.path.join(ip_path, "rtl", f"{ip}.vhd"), "w", encoding="utf-8") as f:
            f.write(rtl_code)
            
        tb_code = tb_tpl.replace("{ip}", ip).replace("{tbsig}", data["tbsig"]).replace("{tbmap}", data["tbmap"]).replace("{tbstim}", data["tbstim"])
        with open(os.path.join(ip_path, "tb", f"tb_{ip}.vhd"), "w", encoding="utf-8") as f:
            f.write(tb_code)
            
        print(f" -> Logica injetada com sucesso em: {ip}")
        
    print("Injecao da Familia 01 concluida!")

if __name__ == "__main__":
    main()