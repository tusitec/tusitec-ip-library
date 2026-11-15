import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-02-com"
    
    # Correção Cirúrgica: Usar porta 'din' para receber parâmetros, idêntico à Família 01
    ips = {
        "tz_com_001_uart": {
            "ch": "0B",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        tx : out std_logic;\n        rx : in std_logic",
            "reset": "tx <= '1';",
            "core": "tx <= din(0);\n        int_data(0) <= rx;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal tx : std_logic;\n    signal rx : std_logic := '1';",
            "tb_map": "din => din, tx => tx, rx => rx,",
            "tb_stim": "din <= x\"0000_0000\"; rx <= '0'; wait for 20 ns; rx <= '1';"
        },
        "tz_com_002_spi_master": {
            "ch": "0C",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        mosi : out std_logic;\n        miso : in std_logic;\n        sck : out std_logic;\n        cs_n : out std_logic",
            "reset": "mosi <= '0'; sck <= '0'; cs_n <= '1';",
            "core": "mosi <= din(0);\n        sck <= clk;\n        cs_n <= din(1);\n        int_data(0) <= miso;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal mosi, sck, cs_n : std_logic;\n    signal miso : std_logic := '0';",
            "tb_map": "din => din, mosi => mosi, miso => miso, sck => sck, cs_n => cs_n,",
            "tb_stim": "miso <= '1'; wait for 20 ns; miso <= '0';"
        },
        "tz_com_003_spi_slave": {
            "ch": "0D",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        mosi : in std_logic;\n        miso : out std_logic;\n        sck : in std_logic;\n        cs_n : in std_logic",
            "reset": "miso <= 'Z';",
            "core": "if cs_n = '0' then miso <= din(0); else miso <= 'Z'; end if;\n        int_data(0) <= mosi;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal mosi, sck : std_logic := '0';\n    signal cs_n : std_logic := '1';\n    signal miso : std_logic;",
            "tb_map": "din => din, mosi => mosi, miso => miso, sck => sck, cs_n => cs_n,",
            "tb_stim": "cs_n <= '0'; mosi <= '1'; wait for 10 ns; sck <= '1'; wait for 10 ns; sck <= '0'; cs_n <= '1';"
        },
        "tz_com_004_i2c_master": {
            "ch": "0E",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        sda : inout std_logic;\n        scl : inout std_logic",
            "reset": "sda <= 'Z'; scl <= 'Z';",
            "core": "if din(0) = '0' then sda <= '0'; else sda <= 'Z'; end if;\n        if din(1) = '0' then scl <= '0'; else scl <= 'Z'; end if;\n        int_data(0) <= sda; int_data(1) <= scl;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal sda, scl : std_logic;",
            "tb_map": "din => din, sda => sda, scl => scl,",
            "tb_stim": "sda <= 'Z'; scl <= 'Z'; wait for 20 ns;"
        },
        "tz_com_005_i2c_slave": {
            "ch": "0F",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        sda : inout std_logic;\n        scl : inout std_logic",
            "reset": "sda <= 'Z'; scl <= 'Z';",
            "core": "if din(0) = '0' then sda <= '0'; else sda <= 'Z'; end if;\n        int_data(0) <= sda; int_data(1) <= scl;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal sda, scl : std_logic;",
            "tb_map": "din => din, sda => sda, scl => scl,",
            "tb_stim": "sda <= 'Z'; scl <= 'Z'; wait for 20 ns;"
        },
        "tz_com_006_i2s": {
            "ch": "10",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        bclk : out std_logic;\n        lrclk : out std_logic;\n        sdata : out std_logic",
            "reset": "bclk <= '0'; lrclk <= '0'; sdata <= '0';",
            "core": "bclk <= clk;\n        lrclk <= din(1);\n        sdata <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal bclk, lrclk, sdata : std_logic;",
            "tb_map": "din => din, bclk => bclk, lrclk => lrclk, sdata => sdata,",
            "tb_stim": "wait for 20 ns;"
        },
        "tz_com_007_can": {
            "ch": "11",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        can_tx : out std_logic;\n        can_rx : in std_logic",
            "reset": "can_tx <= '1';",
            "core": "can_tx <= din(0);\n        int_data(0) <= can_rx;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal can_tx : std_logic;\n    signal can_rx : std_logic := '1';",
            "tb_map": "din => din, can_tx => can_tx, can_rx => can_rx,",
            "tb_stim": "can_rx <= '0'; wait for 20 ns; can_rx <= '1';"
        },
        "tz_com_008_modbus": {
            "ch": "12",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        rs485_tx : out std_logic;\n        rs485_rx : in std_logic;\n        rs485_en : out std_logic",
            "reset": "rs485_tx <= '1'; rs485_en <= '0';",
            "core": "rs485_tx <= din(0);\n        rs485_en <= din(1);\n        int_data(0) <= rs485_rx;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal rs485_tx, rs485_en : std_logic;\n    signal rs485_rx : std_logic := '1';",
            "tb_map": "din => din, rs485_tx => rs485_tx, rs485_rx => rs485_rx, rs485_en => rs485_en,",
            "tb_stim": "rs485_rx <= '0'; wait for 20 ns; rs485_rx <= '1';"
        },
        "tz_com_009_eth_mac": {
            "ch": "13",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        mdc : out std_logic;\n        mdio : inout std_logic;\n        rxd : in std_logic_vector(1 downto 0);\n        txd : out std_logic_vector(1 downto 0)",
            "reset": "mdc <= '0'; mdio <= 'Z'; txd <= \"00\";",
            "core": "mdc <= clk;\n        txd <= din(1 downto 0);\n        int_data(1 downto 0) <= rxd;\n        int_data(2) <= mdio;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal mdc, mdio : std_logic;\n    signal rxd : std_logic_vector(1 downto 0) := \"00\";\n    signal txd : std_logic_vector(1 downto 0);",
            "tb_map": "din => din, mdc => mdc, mdio => mdio, rxd => rxd, txd => txd,",
            "tb_stim": "rxd <= \"01\"; wait for 20 ns; rxd <= \"10\";"
        },
        "tz_com_010_usb": {
            "ch": "14",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        dp : inout std_logic;\n        dm : inout std_logic",
            "reset": "dp <= 'Z'; dm <= 'Z';",
            "core": "if din(2) = '1' then dp <= din(0); dm <= din(1); else dp <= 'Z'; dm <= 'Z'; end if;\n        int_data(0) <= dp; int_data(1) <= dm;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal dp, dm : std_logic;",
            "tb_map": "din => din, dp => dp, dm => dm,",
            "tb_stim": "dp <= 'Z'; dm <= 'Z'; wait for 20 ns; dp <= '1'; dm <= '0'; wait for 20 ns; dp <= 'Z'; dm <= 'Z';"
        }
    }

    rtl_tpl = '''library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.tusitec_tlink_pkg.all;

entity {ip} is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        {ports};
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;

architecture rtl of {ip} is
    signal int_data : std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
    signal v_flag   : std_logic;
begin
    process(clk, rst_n)
    begin
        if rst_n = '0' then
            int_data <= (others => '0');
            v_flag <= '0';
            {reset}
        elsif rising_edge(clk) then
            int_data <= (others => '0');
            v_flag <= '1';
            {core}
        end if;
    end process;

    tlink_tx.valid   <= v_flag;
    tlink_tx.data    <= int_data;
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
    {tb_sigs}
    signal tlink_tx : t_tlink_s2m;
    signal tlink_rx : t_tlink_m2s;
begin
    process begin clk <= '0'; wait for 5 ns; clk <= '1'; wait for 5 ns; end process;

    dut: entity work.{ip}
        port map (
            clk      => clk,
            rst_n    => rst_n,
            {tb_map}
            tlink_tx => tlink_tx,
            tlink_rx => tlink_rx
        );

    process
    begin
        rst_n <= '0'; wait for 20 ns;
        rst_n <= '1'; wait for 20 ns;
        {tb_stim}
        wait;
    end process;
end architecture sim;
'''

    print("Iniciando Injecao Blindada na Familia TZ-02-COM...")
    
    for ip, data in ips.items():
        ip_path = os.path.join(base_dir, ip)
        if not os.path.exists(ip_path): 
            continue
            
        rtl_dir = os.path.join(ip_path, "rtl")
        tb_dir = os.path.join(ip_path, "tb")
        os.makedirs(rtl_dir, exist_ok=True)
        os.makedirs(tb_dir, exist_ok=True)
            
        rtl_code = rtl_tpl.replace("{ip}", ip).replace("{ports}", data["ports"]).replace("{reset}", data["reset"]).replace("{core}", data["core"]).replace("{ch}", data["ch"])
        with open(os.path.join(rtl_dir, f"{ip}.vhd"), "w", encoding="utf-8") as f:
            f.write(rtl_code)
            
        tb_code = tb_tpl.replace("{ip}", ip).replace("{tb_sigs}", data["tb_sigs"]).replace("{tb_map}", data["tb_map"]).replace("{tb_stim}", data["tb_stim"])
        with open(os.path.join(tb_dir, f"tb_{ip}.vhd"), "w", encoding="utf-8") as f:
            f.write(tb_code)
            
        print(f" -> VHDL corrigido e injetado em: {ip}")
        
    print("Injecao da Familia 02 concluida com exito!")

if __name__ == "__main__":
    main()