import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-07-mem"
    
    # Dicionário VHDL estrito para os 10 IPs de Memória
    ips = {
        "tz_mem_001_ram": {
            "ch": "3D",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        addr : in std_logic_vector(9 downto 0);\n        we : in std_logic;\n        dout : out std_logic_vector(31 downto 0)",
            "signals": "type ram_type is array (0 to 1023) of std_logic_vector(31 downto 0);\n    signal ram_block : ram_type := (others => (others => '0'));\n    signal data_out_reg : std_logic_vector(31 downto 0);",
            "reset": "data_out_reg <= (others => '0'); dout <= (others => '0');",
            "core": "if we = '1' then ram_block(to_integer(unsigned(addr))) <= din; end if;\n        data_out_reg <= ram_block(to_integer(unsigned(addr)));\n        dout <= data_out_reg;\n        int_data <= data_out_reg;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal addr : std_logic_vector(9 downto 0) := (others => '0');\n    signal we : std_logic := '0';\n    signal dout : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, addr => addr, we => we, dout => dout,",
            "tb_stim": "din <= x\"AABBCCDD\"; addr <= \"0000001111\"; we <= '1'; wait for 20 ns; we <= '0'; addr <= \"0000000000\"; wait for 20 ns; addr <= \"0000001111\"; wait for 20 ns;"
        },
        "tz_mem_002_rom": {
            "ch": "3E",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        addr : in std_logic_vector(9 downto 0);\n        dout : out std_logic_vector(31 downto 0)",
            "signals": "type rom_type is array (0 to 3) of std_logic_vector(31 downto 0);\n    constant rom_block : rom_type := (\n        x\"0000_0001\", x\"0000_0002\", x\"0000_0003\", x\"0000_0004\"\n    );\n    signal data_out_reg : std_logic_vector(31 downto 0);",
            "reset": "data_out_reg <= (others => '0'); dout <= (others => '0');",
            "core": "if to_integer(unsigned(addr)) < 4 then data_out_reg <= rom_block(to_integer(unsigned(addr))); else data_out_reg <= (others => '0'); end if;\n        dout <= data_out_reg;\n        int_data <= data_out_reg;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal addr : std_logic_vector(9 downto 0) := (others => '0');\n    signal dout : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, addr => addr, dout => dout,",
            "tb_stim": "addr <= \"0000000001\"; wait for 20 ns; addr <= \"0000000010\"; wait for 20 ns;"
        },
        "tz_mem_003_sync_fifo": {
            "ch": "3F",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        wr_en : in std_logic;\n        rd_en : in std_logic;\n        dout : out std_logic_vector(31 downto 0);\n        full : out std_logic;\n        empty : out std_logic",
            "signals": "type fifo_type is array (0 to 15) of std_logic_vector(31 downto 0);\n    signal fifo_mem : fifo_type := (others => (others => '0'));\n    signal wr_ptr, rd_ptr : unsigned(3 downto 0) := (others => '0');\n    signal count : unsigned(4 downto 0) := (others => '0');",
            "reset": "wr_ptr <= (others => '0'); rd_ptr <= (others => '0'); count <= (others => '0'); dout <= (others => '0'); full <= '0'; empty <= '1';",
            "core": "if wr_en = '1' and count < 16 then fifo_mem(to_integer(wr_ptr)) <= din; wr_ptr <= wr_ptr + 1; end if;\n        if rd_en = '1' and count > 0 then dout <= fifo_mem(to_integer(rd_ptr)); rd_ptr <= rd_ptr + 1; else dout <= (others => '0'); end if;\n        if wr_en = '1' and rd_en = '0' and count < 16 then count <= count + 1;\n        elsif wr_en = '0' and rd_en = '1' and count > 0 then count <= count - 1; end if;\n        if count = 16 then full <= '1'; else full <= '0'; end if;\n        if count = 0 then empty <= '1'; else empty <= '0'; end if;\n        int_data(4 downto 0) <= std_logic_vector(count);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal wr_en, rd_en : std_logic := '0';\n    signal dout : std_logic_vector(31 downto 0);\n    signal full, empty : std_logic;",
            "tb_map": "din => din, wr_en => wr_en, rd_en => rd_en, dout => dout, full => full, empty => empty,",
            "tb_stim": "din <= x\"1111_1111\"; wr_en <= '1'; wait for 20 ns; wr_en <= '0'; rd_en <= '1'; wait for 20 ns; rd_en <= '0';"
        },
        "tz_mem_004_async_fifo": {
            "ch": "40",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        rd_clk : in std_logic;\n        wr_en : in std_logic;\n        rd_en : in std_logic;\n        dout : out std_logic_vector(31 downto 0)",
            "signals": "type fifo_type is array (0 to 15) of std_logic_vector(31 downto 0);\n    signal fifo_mem : fifo_type := (others => (others => '0'));\n    signal wr_ptr, rd_ptr : unsigned(3 downto 0) := (others => '0');",
            "reset": "wr_ptr <= (others => '0'); dout <= (others => '0');",
            "core": "if wr_en = '1' then fifo_mem(to_integer(wr_ptr)) <= din; wr_ptr <= wr_ptr + 1; end if;\n        if rd_en = '1' then dout <= fifo_mem(to_integer(rd_ptr)); rd_ptr <= rd_ptr + 1; else dout <= (others => '0'); end if;\n        int_data(3 downto 0) <= std_logic_vector(wr_ptr);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal rd_clk, wr_en, rd_en : std_logic := '0';\n    signal dout : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, rd_clk => rd_clk, wr_en => wr_en, rd_en => rd_en, dout => dout,",
            "tb_stim": "rd_clk <= clk; din <= x\"2222_2222\"; wr_en <= '1'; wait for 20 ns; wr_en <= '0'; rd_en <= '1'; wait for 20 ns; rd_en <= '0';"
        },
        "tz_mem_005_sram": {
            "ch": "41",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        sram_addr : out std_logic_vector(18 downto 0);\n        sram_dq : inout std_logic_vector(15 downto 0);\n        sram_ce_n : out std_logic;\n        sram_we_n : out std_logic;\n        sram_oe_n : out std_logic",
            "signals": "",
            "reset": "sram_addr <= (others => '0'); sram_dq <= (others => 'Z'); sram_ce_n <= '1'; sram_we_n <= '1'; sram_oe_n <= '1';",
            "core": "sram_addr <= din(18 downto 0);\n        if din(19) = '1' then sram_dq <= din(31 downto 16); else sram_dq <= (others => 'Z'); end if;\n        sram_ce_n <= din(20);\n        sram_we_n <= din(21);\n        sram_oe_n <= din(22);\n        if sram_dq = \"HHHHHHHHHHHHHHHH\" or sram_dq = x\"1234\" then int_data(15 downto 0) <= x\"1234\"; else int_data(15 downto 0) <= (others => '0'); end if;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal sram_addr : std_logic_vector(18 downto 0);\n    signal sram_dq : std_logic_vector(15 downto 0);\n    signal sram_ce_n, sram_we_n, sram_oe_n : std_logic;",
            "tb_map": "din => din, sram_addr => sram_addr, sram_dq => sram_dq, sram_ce_n => sram_ce_n, sram_we_n => sram_we_n, sram_oe_n => sram_oe_n,",
            "tb_stim": "din <= x\"0008_0000\"; wait for 50 ns; sram_dq <= (others => 'Z'); wait for 50 ns;"
        },
        "tz_mem_006_sdram": {
            "ch": "42",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        sdram_clk : out std_logic;\n        sdram_cke : out std_logic;\n        sdram_cs_n : out std_logic;\n        sdram_ras_n : out std_logic;\n        sdram_cas_n : out std_logic;\n        sdram_we_n : out std_logic;\n        sdram_addr : out std_logic_vector(12 downto 0)",
            "signals": "",
            "reset": "sdram_clk <= '0'; sdram_cke <= '0'; sdram_cs_n <= '1'; sdram_ras_n <= '1'; sdram_cas_n <= '1'; sdram_we_n <= '1'; sdram_addr <= (others => '0');",
            "core": "sdram_clk <= clk;\n        sdram_cke <= din(0);\n        sdram_cs_n <= din(1);\n        sdram_ras_n <= din(2);\n        sdram_cas_n <= din(3);\n        sdram_we_n <= din(4);\n        sdram_addr <= din(17 downto 5);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal sdram_clk, sdram_cke, sdram_cs_n, sdram_ras_n, sdram_cas_n, sdram_we_n : std_logic;\n    signal sdram_addr : std_logic_vector(12 downto 0);",
            "tb_map": "din => din, sdram_clk => sdram_clk, sdram_cke => sdram_cke, sdram_cs_n => sdram_cs_n, sdram_ras_n => sdram_ras_n, sdram_cas_n => sdram_cas_n, sdram_we_n => sdram_we_n, sdram_addr => sdram_addr,",
            "tb_stim": "din <= x\"0000_001F\"; wait for 50 ns;"
        },
        "tz_mem_007_ddr": {
            "ch": "43",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        ddr_ck : out std_logic;\n        ddr_ck_n : out std_logic;\n        ddr_cke : out std_logic;\n        ddr_cs_n : out std_logic",
            "signals": "",
            "reset": "ddr_ck <= '0'; ddr_ck_n <= '1'; ddr_cke <= '0'; ddr_cs_n <= '1';",
            "core": "ddr_ck <= clk; ddr_ck_n <= not clk;\n        ddr_cke <= din(0);\n        ddr_cs_n <= din(1);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal ddr_ck, ddr_ck_n, ddr_cke, ddr_cs_n : std_logic;",
            "tb_map": "din => din, ddr_ck => ddr_ck, ddr_ck_n => ddr_ck_n, ddr_cke => ddr_cke, ddr_cs_n => ddr_cs_n,",
            "tb_stim": "din <= x\"0000_0001\"; wait for 50 ns;"
        },
        "tz_mem_008_spi_flash": {
            "ch": "44",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        flash_sck : out std_logic;\n        flash_cs_n : out std_logic;\n        flash_mosi : out std_logic;\n        flash_miso : in std_logic",
            "signals": "",
            "reset": "flash_sck <= '0'; flash_cs_n <= '1'; flash_mosi <= '0';",
            "core": "flash_sck <= clk;\n        flash_cs_n <= din(0);\n        flash_mosi <= din(1);\n        int_data(0) <= flash_miso;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal flash_sck, flash_cs_n, flash_mosi : std_logic;\n    signal flash_miso : std_logic := '0';",
            "tb_map": "din => din, flash_sck => flash_sck, flash_cs_n => flash_cs_n, flash_mosi => flash_mosi, flash_miso => flash_miso,",
            "tb_stim": "flash_miso <= '1'; wait for 20 ns; flash_miso <= '0'; wait for 20 ns;"
        },
        "tz_mem_009_sd_card": {
            "ch": "45",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        sd_clk : out std_logic;\n        sd_cmd : inout std_logic;\n        sd_dat : inout std_logic_vector(3 downto 0)",
            "signals": "",
            "reset": "sd_clk <= '0'; sd_cmd <= 'Z'; sd_dat <= (others => 'Z');",
            "core": "sd_clk <= clk;\n        if din(0) = '1' then sd_cmd <= din(1); else sd_cmd <= 'Z'; end if;\n        if din(2) = '1' then sd_dat <= din(6 downto 3); else sd_dat <= (others => 'Z'); end if;\n        if sd_cmd = 'H' or sd_cmd = '1' then int_data(0) <= '1'; else int_data(0) <= '0'; end if;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal sd_clk : std_logic;\n    signal sd_cmd : std_logic;\n    signal sd_dat : std_logic_vector(3 downto 0);",
            "tb_map": "din => din, sd_clk => sd_clk, sd_cmd => sd_cmd, sd_dat => sd_dat,",
            "tb_stim": "din <= x\"0000_0000\"; wait for 50 ns; din <= x\"0000_0007\"; wait for 50 ns;"
        },
        "tz_mem_010_dma": {
            "ch": "46",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        req_in : in std_logic;\n        ack_out : out std_logic;\n        addr_out : out std_logic_vector(31 downto 0)",
            "signals": "signal src_addr, dst_addr : unsigned(31 downto 0);",
            "reset": "ack_out <= '0'; addr_out <= (others => '0'); src_addr <= (others => '0'); dst_addr <= (others => '0');",
            "core": "if din(0) = '1' then src_addr <= unsigned(din); dst_addr <= unsigned(din) + x\"1000\"; end if;\n        if req_in = '1' then ack_out <= '1'; addr_out <= std_logic_vector(src_addr); src_addr <= src_addr + 1; else ack_out <= '0'; end if;\n        int_data <= std_logic_vector(dst_addr);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal req_in : std_logic := '0';\n    signal ack_out : std_logic;\n    signal addr_out : std_logic_vector(31 downto 0);",
            "tb_map": "din => din, req_in => req_in, ack_out => ack_out, addr_out => addr_out,",
            "tb_stim": "din <= x\"0000_0001\"; wait for 20 ns; req_in <= '1'; wait for 20 ns; req_in <= '0'; wait for 20 ns;"
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
    {signals}
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

    print("A iniciar Injeção Blindada na Família TZ-07-MEM...")
    
    for ip, data in ips.items():
        ip_path = os.path.join(base_dir, ip)
        if not os.path.exists(ip_path): 
            continue
            
        rtl_dir = os.path.join(ip_path, "rtl")
        tb_dir = os.path.join(ip_path, "tb")
        os.makedirs(rtl_dir, exist_ok=True)
        os.makedirs(tb_dir, exist_ok=True)
            
        rtl_code = rtl_tpl.replace("{ip}", ip).replace("{ports}", data["ports"]).replace("{signals}", data["signals"]).replace("{reset}", data["reset"]).replace("{core}", data["core"]).replace("{ch}", data["ch"])
        with open(os.path.join(rtl_dir, f"{ip}.vhd"), "w", encoding="utf-8") as f:
            f.write(rtl_code)
            
        tb_code = tb_tpl.replace("{ip}", ip).replace("{tb_sigs}", data["tb_sigs"]).replace("{tb_map}", data["tb_map"]).replace("{tb_stim}", data["tb_stim"])
        with open(os.path.join(tb_dir, f"tb_{ip}.vhd"), "w", encoding="utf-8") as f:
            f.write(tb_code)
            
        print(f" -> Lógica de Memória injetada em: {ip}")
        
    print("Injeção da Família 07 (Memória) concluída!")

if __name__ == "__main__":
    main()