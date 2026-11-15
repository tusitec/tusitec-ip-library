import os

def main():
    base_dir = r"F:\projetos\tusitec-ip-library\tz-05-vid"
    
    # Dicionário VHDL estrito para os 10 IPs de Vídeo
    ips = {
        "tz_vid_001_vga": {
            "ch": "29",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        hsync : out std_logic;\n        vsync : out std_logic;\n        rgb : out std_logic_vector(23 downto 0)",
            "signals": "",
            "reset": "hsync <= '0'; vsync <= '0'; rgb <= (others => '0');",
            "core": "hsync <= din(24);\n        vsync <= din(25);\n        rgb <= din(23 downto 0);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal hsync, vsync : std_logic;\n    signal rgb : std_logic_vector(23 downto 0);",
            "tb_map": "din => din, hsync => hsync, vsync => vsync, rgb => rgb,",
            "tb_stim": "din <= x\"03AABBCC\"; wait for 50 ns;"
        },
        "tz_vid_002_char_gen": {
            "ch": "2A",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        char_code : in std_logic_vector(7 downto 0);\n        pixel_out : out std_logic",
            "signals": "",
            "reset": "pixel_out <= '0';",
            "core": "if char_code = x\"41\" then pixel_out <= din(0); else pixel_out <= '0'; end if;\n        int_data(7 downto 0) <= char_code;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal char_code : std_logic_vector(7 downto 0) := x\"00\";\n    signal pixel_out : std_logic;",
            "tb_map": "din => din, char_code => char_code, pixel_out => pixel_out,",
            "tb_stim": "din <= x\"0000_0001\"; char_code <= x\"41\"; wait for 50 ns; char_code <= x\"42\"; wait for 50 ns;"
        },
        "tz_vid_003_lcd": {
            "ch": "2B",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        lcd_rs : out std_logic;\n        lcd_en : out std_logic;\n        lcd_data : out std_logic_vector(7 downto 0)",
            "signals": "",
            "reset": "lcd_rs <= '0'; lcd_en <= '0'; lcd_data <= (others => '0');",
            "core": "lcd_rs <= din(8);\n        lcd_en <= din(9);\n        lcd_data <= din(7 downto 0);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal lcd_rs, lcd_en : std_logic;\n    signal lcd_data : std_logic_vector(7 downto 0);",
            "tb_map": "din => din, lcd_rs => lcd_rs, lcd_en => lcd_en, lcd_data => lcd_data,",
            "tb_stim": "din <= x\"0000_0341\"; wait for 50 ns;"
        },
        "tz_vid_004_oled": {
            "ch": "2C",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        oled_sck : out std_logic;\n        oled_sda : out std_logic;\n        oled_dc : out std_logic;\n        oled_cs : out std_logic",
            "signals": "",
            "reset": "oled_sck <= '0'; oled_sda <= '0'; oled_dc <= '0'; oled_cs <= '1';",
            "core": "oled_sck <= clk;\n        oled_sda <= din(0);\n        oled_dc <= din(1);\n        oled_cs <= din(2);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal oled_sck, oled_sda, oled_dc, oled_cs : std_logic;",
            "tb_map": "din => din, oled_sck => oled_sck, oled_sda => oled_sda, oled_dc => oled_dc, oled_cs => oled_cs,",
            "tb_stim": "din <= x\"0000_0003\"; wait for 50 ns;"
        },
        "tz_vid_005_led_mat": {
            "ch": "2D",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        row_sel : out std_logic_vector(7 downto 0);\n        col_data : out std_logic_vector(7 downto 0)",
            "signals": "",
            "reset": "row_sel <= (others => '0'); col_data <= (others => '0');",
            "core": "row_sel <= din(15 downto 8);\n        col_data <= din(7 downto 0);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal row_sel, col_data : std_logic_vector(7 downto 0);",
            "tb_map": "din => din, row_sel => row_sel, col_data => col_data,",
            "tb_stim": "din <= x\"0000_01FF\"; wait for 50 ns;"
        },
        "tz_vid_006_2d_gfx": {
            "ch": "2E",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        x_coord : in std_logic_vector(9 downto 0);\n        y_coord : in std_logic_vector(9 downto 0);\n        pixel_color : out std_logic_vector(23 downto 0)",
            "signals": "",
            "reset": "pixel_color <= (others => '0');",
            "core": "if x_coord = din(9 downto 0) then pixel_color <= x\"FFFFFF\"; else pixel_color <= x\"000000\"; end if;\n        int_data(9 downto 0) <= x_coord;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal x_coord, y_coord : std_logic_vector(9 downto 0) := (others => '0');\n    signal pixel_color : std_logic_vector(23 downto 0);",
            "tb_map": "din => din, x_coord => x_coord, y_coord => y_coord, pixel_color => pixel_color,",
            "tb_stim": "din <= x\"0000_000A\"; x_coord <= \"0000001010\"; wait for 50 ns; x_coord <= \"0000000000\"; wait for 50 ns;"
        },
        "tz_vid_007_framebuf": {
            "ch": "2F",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        addr : in std_logic_vector(15 downto 0);\n        data_out : out std_logic_vector(15 downto 0)",
            "signals": "",
            "reset": "data_out <= (others => '0');",
            "core": "data_out <= din(15 downto 0);\n        int_data(15 downto 0) <= addr;",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal addr : std_logic_vector(15 downto 0) := (others => '0');\n    signal data_out : std_logic_vector(15 downto 0);",
            "tb_map": "din => din, addr => addr, data_out => data_out,",
            "tb_stim": "din <= x\"0000_FFFF\"; addr <= x\"1024\"; wait for 50 ns;"
        },
        "tz_vid_008_shape_gen": {
            "ch": "30",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        shape_act : out std_logic",
            "signals": "",
            "reset": "shape_act <= '0';",
            "core": "shape_act <= din(0);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal shape_act : std_logic;",
            "tb_map": "din => din, shape_act => shape_act,",
            "tb_stim": "din <= x\"0000_0001\"; wait for 50 ns;"
        },
        "tz_vid_009_hdmi": {
            "ch": "31",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        tmds_clk : out std_logic;\n        tmds_d0 : out std_logic;\n        tmds_d1 : out std_logic;\n        tmds_d2 : out std_logic",
            "signals": "",
            "reset": "tmds_clk <= '0'; tmds_d0 <= '0'; tmds_d1 <= '0'; tmds_d2 <= '0';",
            "core": "tmds_clk <= clk;\n        tmds_d0 <= din(0);\n        tmds_d1 <= din(1);\n        tmds_d2 <= din(2);\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal tmds_clk, tmds_d0, tmds_d1, tmds_d2 : std_logic;",
            "tb_map": "din => din, tmds_clk => tmds_clk, tmds_d0 => tmds_d0, tmds_d1 => tmds_d1, tmds_d2 => tmds_d2,",
            "tb_stim": "din <= x\"0000_0007\"; wait for 50 ns;"
        },
        "tz_vid_010_pix_fmt": {
            "ch": "32",
            "ports": "din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);\n        rgb565 : in std_logic_vector(15 downto 0);\n        rgb888 : out std_logic_vector(23 downto 0)",
            "signals": "",
            "reset": "rgb888 <= (others => '0');",
            "core": "rgb888(23 downto 19) <= rgb565(15 downto 11);\n        rgb888(18 downto 16) <= \"000\";\n        rgb888(15 downto 10) <= rgb565(10 downto 5);\n        rgb888(9 downto 8) <= \"00\";\n        rgb888(7 downto 3) <= rgb565(4 downto 0);\n        rgb888(2 downto 0) <= \"000\";\n        int_data(0) <= din(0);",
            "tb_sigs": "signal din : std_logic_vector(31 downto 0) := (others => '0');\n    signal rgb565 : std_logic_vector(15 downto 0) := (others => '0');\n    signal rgb888 : std_logic_vector(23 downto 0);",
            "tb_map": "din => din, rgb565 => rgb565, rgb888 => rgb888,",
            "tb_stim": "rgb565 <= x\"F800\"; wait for 50 ns; rgb565 <= x\"07E0\"; wait for 50 ns;"
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

    print("A iniciar Injeção Blindada na Família TZ-05-VID...")
    
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
            
        print(f" -> Lógica de Vídeo injetada em: {ip}")
        
    print("Injeção da Família 05 (Vídeo) concluída!")

if __name__ == "__main__":
    main()