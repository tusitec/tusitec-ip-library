import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-00-hub\operador_meec_hub"
    rtl_dir = os.path.join(base_dir, "rtl")
    tb_dir = os.path.join(base_dir, "tb")
    os.makedirs(rtl_dir, exist_ok=True)
    os.makedirs(tb_dir, exist_ok=True)

    rtl_code = '''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity operador_meec_hub is
    generic (
        -- Enderecos dos 4 Satelites mapeados para roteamento
        CH_SAT0 : std_logic_vector(7 downto 0) := x"0B"; -- Ex: tz_com_001_uart
        CH_SAT1 : std_logic_vector(7 downto 0) := x"15"; -- Ex: tz_ctl_001_pwm
        CH_SAT2 : std_logic_vector(7 downto 0) := x"33"; -- Ex: tz_dsp_001_fir
        CH_SAT3 : std_logic_vector(7 downto 0) := x"3D"  -- Ex: tz_mem_001_ram
    );
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        
        -- Barramento T-Link com o Cérebro Central (Operador M*)
        m_tlink_rx : in  t_tlink_m2s;
        m_tlink_tx : out t_tlink_s2m;
        
        -- Tentaculos para o Satelite 0
        sat0_din   : out std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sat0_tx    : in  t_tlink_s2m;
        sat0_rx    : out t_tlink_m2s;
        
        -- Tentaculos para o Satelite 1
        sat1_din   : out std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sat1_tx    : in  t_tlink_s2m;
        sat1_rx    : out t_tlink_m2s;
        
        -- Tentaculos para o Satelite 2
        sat2_din   : out std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sat2_tx    : in  t_tlink_s2m;
        sat2_rx    : out t_tlink_m2s;
        
        -- Tentaculos para o Satelite 3
        sat3_din   : out std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sat3_tx    : in  t_tlink_s2m;
        sat3_rx    : out t_tlink_m2s
    );
end entity operador_meec_hub;

architecture rtl of operador_meec_hub is
    -- Registradores internos de roteamento
    signal reg_din_0, reg_din_1, reg_din_2, reg_din_3 : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
begin

    -- 1. ROTEAMENTO DE IDA (Demultiplexador: Master -> Satelites)
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            reg_din_0 <= (others => '0');
            reg_din_1 <= (others => '0');
            reg_din_2 <= (others => '0');
            reg_din_3 <= (others => '0');
        elsif rising_edge(clk) then
            if m_tlink_rx.valid = '1' then
                -- O Hub le a etiqueta (channel) e encaminha apenas para o satelite correto
                case m_tlink_rx.channel is
                    when CH_SAT0 => reg_din_0 <= m_tlink_rx.data;
                    when CH_SAT1 => reg_din_1 <= m_tlink_rx.data;
                    when CH_SAT2 => reg_din_2 <= m_tlink_rx.data;
                    when CH_SAT3 => reg_din_3 <= m_tlink_rx.data;
                    when others  => null;
                end case;
            end if;
        end if;
    end process;
    
    -- Aplica os dados roteados nas portas fisicas dos satelites
    sat0_din <= reg_din_0;
    sat1_din <= reg_din_1;
    sat2_din <= reg_din_2;
    sat3_din <= reg_din_3;
    
    -- Bypass estrito para compatibilidade de blocos
    sat0_rx <= m_tlink_rx; sat1_rx <= m_tlink_rx; sat2_rx <= m_tlink_rx; sat3_rx <= m_tlink_rx;

    -- 2. ROTEAMENTO DE VOLTA (Multiplexador: Satelites -> Master)
    process(sat0_tx, sat1_tx, sat2_tx, sat3_tx)
    begin
        -- Silencio no barramento por defeito
        m_tlink_tx.valid   <= '0';
        m_tlink_tx.data    <= (others => '0');
        m_tlink_tx.channel <= (others => '0');
        m_tlink_tx.sop     <= '0';
        m_tlink_tx.eop     <= '0';
        
        -- Ouve qual satelite gritou "Valid = 1" e interliga-o ao Mestre
        if sat0_tx.valid = '1' then
            m_tlink_tx <= sat0_tx;
        elsif sat1_tx.valid = '1' then
            m_tlink_tx <= sat1_tx;
        elsif sat2_tx.valid = '1' then
            m_tlink_tx <= sat2_tx;
        elsif sat3_tx.valid = '1' then
            m_tlink_tx <= sat3_tx;
        end if;
    end process;

end architecture rtl;
'''

    tb_code = '''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity tb_operador_meec_hub is
end entity;

architecture sim of tb_operador_meec_hub is
    signal clk      : std_logic := '0';
    signal rst_n    : std_logic := '0';
    
    signal m_rx : t_tlink_m2s;
    signal m_tx : t_tlink_s2m;
    
    signal s0_din, s1_din, s2_din, s3_din : std_logic_vector(31 downto 0);
    signal s0_tx, s1_tx, s2_tx, s3_tx : t_tlink_s2m := ('0', (others => '0'), (others => '0'), '0', '0');
    signal s0_rx, s1_rx, s2_rx, s3_rx : t_tlink_m2s;
    
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.operador_meec_hub
        generic map (
            CH_SAT0 => x"0B", CH_SAT1 => x"15", CH_SAT2 => x"33", CH_SAT3 => x"3D"
        )
        port map (
            clk => clk, rst_n => rst_n,
            m_tlink_rx => m_rx, m_tlink_tx => m_tx,
            sat0_din => s0_din, sat0_tx => s0_tx, sat0_rx => s0_rx,
            sat1_din => s1_din, sat1_tx => s1_tx, sat1_rx => s1_rx,
            sat2_din => s2_din, sat2_tx => s2_tx, sat2_rx => s2_rx,
            sat3_din => s3_din, sat3_tx => s3_tx, sat3_rx => s3_rx
        );

    process
    begin
        rst_n <= '0'; 
        m_rx.valid <= '0'; m_rx.data <= (others => '0'); m_rx.channel <= (others => '0');
        wait for 20 ns;
        
        rst_n <= '1'; 
        wait for 20 ns;
        
        -- Teste: O Mestre (Operador M*) quer falar com o PWM (Canal x15)
        m_rx.valid <= '1';
        m_rx.channel <= x"15";
        m_rx.data <= x"DEADBEEF";
        wait for 10 ns;
        m_rx.valid <= '0';
        wait for 40 ns;
        
        -- Teste: A RAM (Satelite 3, Canal x3D) envia um dado de volta ao Mestre
        s3_tx.valid <= '1';
        s3_tx.channel <= x"3D";
        s3_tx.data <= x"CAFEBABE";
        wait for 10 ns;
        s3_tx.valid <= '0';
        
        wait;
    end process;
end architecture sim;
'''
    
    with open(os.path.join(rtl_dir, "operador_meec_hub.vhd"), "w", encoding="utf-8") as f:
        f.write(rtl_code)
        
    with open(os.path.join(tb_dir, "tb_operador_meec_hub.vhd"), "w", encoding="utf-8") as f:
        f.write(tb_code)
        
    print("O roteador 'operador_meec_hub' (4 canais) foi forjado com sucesso!")

if __name__ == "__main__":
    main()