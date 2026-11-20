# Tusitec Silicon Library — T-Link IP Cores

Repositório oficial da biblioteca de propriedade intelectual em hardware (**VHDL RTL**) desenvolvida pela **Tusitec Ltda** (`tusitec.com.br`).

Todos os **100 IP Cores** seguem a arquitetura modular **Zero-DSP** com interface nativa para o barramento proprietário **T-Link** (`tusitec_tlink_pkg`) e validação 100% aprovada via simulação **GHDL**.

---

## Catálogo de Famílias (100 IP Cores)

### `tz-01-log` — Lógica e Aritmética
Blocos fundamentais de lógica digital, contadores, ULAs e máquinas de estados.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_log_001_mux`** | `0x01` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_001_mux/README.md) |
| **`tz_log_002_counter`** | `0x02` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_002_counter/README.md) |
| **`tz_log_003_freqdiv`** | `0x03` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_003_freqdiv/README.md) |
| **`tz_log_004_shiftreg`** | `0x04` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_004_shiftreg/README.md) |
| **`tz_log_005_comparator`** | `0x05` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_005_comparator/README.md) |
| **`tz_log_006_decoder`** | `0x06` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_006_decoder/README.md) |
| **`tz_log_007_alu`** | `0x07` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_007_alu/README.md) |
| **`tz_log_008_fsm`** | `0x08` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_008_fsm/README.md) |
| **`tz_log_009_pulsegen`** | `0x09` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_009_pulsegen/README.md) |
| **`tz_log_010_widthconv`** | `0x0A` | `PASS` | [Ver Datasheet](./tz-01-log/tz_log_010_widthconv/README.md) |


### `tz-02-com` — Comunicação e Protocolos
Interfaces seriais e paralelas (UART, SPI, I2C, CAN, Ethernet/MDIO).

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_com_001_uart`** | `0x0B` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_001_uart/README.md) |
| **`tz_com_002_spi_master`** | `0x0C` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_002_spi_master/README.md) |
| **`tz_com_003_spi_slave`** | `0x0D` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_003_spi_slave/README.md) |
| **`tz_com_004_i2c_master`** | `0x0E` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_004_i2c_master/README.md) |
| **`tz_com_005_i2c_slave`** | `0x0F` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_005_i2c_slave/README.md) |
| **`tz_com_006_i2s`** | `0x10` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_006_i2s/README.md) |
| **`tz_com_007_can`** | `0x11` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_007_can/README.md) |
| **`tz_com_008_modbus`** | `0x12` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_008_modbus/README.md) |
| **`tz_com_009_eth_mac`** | `0x13` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_009_eth_mac/README.md) |
| **`tz_com_010_usb`** | `0x14` | `PASS` | [Ver Datasheet](./tz-02-com/tz_com_010_usb/README.md) |


### `tz-03-ctl` — Controle e Automação
Modulação PWM, controle PID, acionamento de motores de passo e servomecanismos.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_ctl_001_pwm`** | `0x15` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_001_pwm/README.md) |
| **`tz_ctl_002_comp_pwm`** | `0x16` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_002_comp_pwm/README.md) |
| **`tz_ctl_003_dead_time`** | `0x17` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_003_dead_time/README.md) |
| **`tz_ctl_004_dc_motor`** | `0x18` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_004_dc_motor/README.md) |
| **`tz_ctl_005_stepper`** | `0x19` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_005_stepper/README.md) |
| **`tz_ctl_006_servo`** | `0x1A` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_006_servo/README.md) |
| **`tz_ctl_007_encoder`** | `0x1B` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_007_encoder/README.md) |
| **`tz_ctl_008_pid`** | `0x1C` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_008_pid/README.md) |
| **`tz_ctl_009_watchdog`** | `0x1D` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_009_watchdog/README.md) |
| **`tz_ctl_010_counter`** | `0x1E` | `PASS` | [Ver Datasheet](./tz-03-ctl/tz_ctl_010_counter/README.md) |


### `tz-04-aqd` — Aquisição de Dados
Interfaces de leitura de conversores ADC/DAC, sensores digitais e amostragem.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_aqd_001_adc`** | `0x1F` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_001_adc/README.md) |
| **`tz_aqd_002_dac`** | `0x20` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_002_dac/README.md) |
| **`tz_aqd_003_dig_sensor`** | `0x21` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_003_dig_sensor/README.md) |
| **`tz_aqd_004_ana_acq`** | `0x22` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_004_ana_acq/README.md) |
| **`tz_aqd_005_pulse_cap`** | `0x23` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_005_pulse_cap/README.md) |
| **`tz_aqd_006_freq_meter`** | `0x24` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_006_freq_meter/README.md) |
| **`tz_aqd_007_per_meter`** | `0x25` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_007_per_meter/README.md) |
| **`tz_aqd_008_duty_meter`** | `0x26` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_008_duty_meter/README.md) |
| **`tz_aqd_009_multi_acq`** | `0x27` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_009_multi_acq/README.md) |
| **`tz_aqd_010_timestamp`** | `0x28` | `PASS` | [Ver Datasheet](./tz-04-aqd/tz_aqd_010_timestamp/README.md) |


### `tz-05-vid` — Vídeo e Imagem
Controladores de sincronismo VGA/HDMI, buffers de linha e processamento de pixels.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_vid_001_vga`** | `0x29` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_001_vga/README.md) |
| **`tz_vid_002_char_gen`** | `0x2A` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_002_char_gen/README.md) |
| **`tz_vid_003_lcd`** | `0x2B` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_003_lcd/README.md) |
| **`tz_vid_004_oled`** | `0x2C` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_004_oled/README.md) |
| **`tz_vid_005_led_mat`** | `0x2D` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_005_led_mat/README.md) |
| **`tz_vid_006_2d_gfx`** | `0x2E` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_006_2d_gfx/README.md) |
| **`tz_vid_007_framebuf`** | `0x2F` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_007_framebuf/README.md) |
| **`tz_vid_008_shape_gen`** | `0x30` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_008_shape_gen/README.md) |
| **`tz_vid_009_hdmi`** | `0x31` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_009_hdmi/README.md) |
| **`tz_vid_010_pix_fmt`** | `0x32` | `PASS` | [Ver Datasheet](./tz-05-vid/tz_vid_010_pix_fmt/README.md) |


### `tz-06-dsp` — Processamento Digital de Sinais (DSP)
Filtros FIR/IIR, transformadas rápidas e aritmética de sinais Zero-DSP.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_dsp_001_fir`** | `0x33` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_001_fir/README.md) |
| **`tz_dsp_002_iir`** | `0x34` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_002_iir/README.md) |
| **`tz_dsp_003_fft`** | `0x35` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_003_fft/README.md) |
| **`tz_dsp_004_ifft`** | `0x36` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_004_ifft/README.md) |
| **`tz_dsp_005_mac`** | `0x37` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_005_mac/README.md) |
| **`tz_dsp_006_dds`** | `0x38` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_006_dds/README.md) |
| **`tz_dsp_007_cordic`** | `0x39` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_007_cordic/README.md) |
| **`tz_dsp_008_freq_det`** | `0x3A` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_008_freq_det/README.md) |
| **`tz_dsp_009_modulator`** | `0x3B` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_009_modulator/README.md) |
| **`tz_dsp_010_demodulator`** | `0x3C` | `PASS` | [Ver Datasheet](./tz-06-dsp/tz_dsp_010_demodulator/README.md) |


### `tz-07-mem` — Memória e Armazenamento
Controladores de RAM, FIFOs síncronas, caches e motores de transferência.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_mem_001_ram`** | `0x3D` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_001_ram/README.md) |
| **`tz_mem_002_rom`** | `0x3E` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_002_rom/README.md) |
| **`tz_mem_003_sync_fifo`** | `0x3F` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_003_sync_fifo/README.md) |
| **`tz_mem_004_async_fifo`** | `0x40` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_004_async_fifo/README.md) |
| **`tz_mem_005_sram`** | `0x41` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_005_sram/README.md) |
| **`tz_mem_006_sdram`** | `0x42` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_006_sdram/README.md) |
| **`tz_mem_007_ddr`** | `0x43` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_007_ddr/README.md) |
| **`tz_mem_008_spi_flash`** | `0x44` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_008_spi_flash/README.md) |
| **`tz_mem_009_sd_card`** | `0x45` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_009_sd_card/README.md) |
| **`tz_mem_010_dma`** | `0x46` | `PASS` | [Ver Datasheet](./tz-07-mem/tz_mem_010_dma/README.md) |


### `tz-08-sys` — Sistemas e Infraestrutura
Timers, Watchdogs, controladores de interrupção e gestão de barramento.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_sys_001_softcore`** | `0x47` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_001_softcore/README.md) |
| **`tz_sys_002_riscv`** | `0x48` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_002_riscv/README.md) |
| **`tz_sys_003_int_ctrl`** | `0x49` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_003_int_ctrl/README.md) |
| **`tz_sys_004_int_bus`** | `0x4A` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_004_int_bus/README.md) |
| **`tz_sys_005_axi4_lite`** | `0x4B` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_005_axi4_lite/README.md) |
| **`tz_sys_006_avalon`** | `0x4C` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_006_avalon/README.md) |
| **`tz_sys_007_wishbone`** | `0x4D` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_007_wishbone/README.md) |
| **`tz_sys_008_reg_bank`** | `0x4E` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_008_reg_bank/README.md) |
| **`tz_sys_009_soc_interconnect`** | `0x4F` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_009_soc_interconnect/README.md) |
| **`tz_sys_010_bus_bridge`** | `0x50` | `PASS` | [Ver Datasheet](./tz-08-sys/tz_sys_010_bus_bridge/README.md) |


### `tz-09-dbg` — Debug e Verificação
Analisadores lógicos in-chip, geradores PRBS, cálculo de CRC e monitores de performance.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`tz_dbg_001_logic_ana`** | `0x51` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_001_logic_ana/README.md) |
| **`tz_dbg_002_pat_gen`** | `0x52` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_002_pat_gen/README.md) |
| **`tz_dbg_003_test_sig`** | `0x53` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_003_test_sig/README.md) |
| **`tz_dbg_004_wave_cap`** | `0x54` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_004_wave_cap/README.md) |
| **`tz_dbg_005_err_count`** | `0x55` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_005_err_count/README.md) |
| **`tz_dbg_006_crc`** | `0x56` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_006_crc/README.md) |
| **`tz_dbg_007_prbs`** | `0x57` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_007_prbs/README.md) |
| **`tz_dbg_008_perf_mon`** | `0x58` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_008_perf_mon/README.md) |
| **`tz_dbg_009_bus_mon`** | `0x59` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_009_bus_mon/README.md) |
| **`tz_dbg_010_trigger`** | `0x5A` | `PASS` | [Ver Datasheet](./tz-09-dbg/tz_dbg_010_trigger/README.md) |


### `tz-10-esp` — IP Cores Especializados
Fusão de sensores, robótica, navegação autônoma, criptografia AES, visão computacional e aceleradores neurais.

| Módulo IP Core | Canal T-Link | Status GHDL | Documentação |
| :--- | :---: | :---: | :---: |
| **`fusao-sensores`** | `N/A` | `PASS` | [Ver Datasheet](./tz-10-esp/fusao-sensores/README.md) |
| **`tz_esp_001_sensor_fusion`** | `0x5B` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_001_sensor_fusion/README.md) |
| **`tz_esp_002_robotics`** | `0x5C` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_002_robotics/README.md) |
| **`tz_esp_003_auto_nav`** | `0x5D` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_003_auto_nav/README.md) |
| **`tz_esp_004_aes`** | `0x5E` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_004_aes/README.md) |
| **`tz_esp_005_err_corr`** | `0x5F` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_005_err_corr/README.md) |
| **`tz_esp_006_cv_engine`** | `0x60` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_006_cv_engine/README.md) |
| **`tz_esp_007_ind_net`** | `0x61` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_007_ind_net/README.md) |
| **`tz_esp_008_sci_inst`** | `0x62` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_008_sci_inst/README.md) |
| **`tz_esp_009_telecom_dsp`** | `0x63` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_009_telecom_dsp/README.md) |
| **`tz_esp_010_nn_accel`** | `0x64` | `PASS` | [Ver Datasheet](./tz-10-esp/tz_esp_010_nn_accel/README.md) |
| **`visao-computacional`** | `N/A` | `PASS` | [Ver Datasheet](./tz-10-esp/visao-computacional/README.md) |


---

## Documentação Técnica — Portal do Desenvolvedor

| Seção | Foco Técnico | Referência no Portal (`tusitec.com.br`) |
| :--- | :--- | :--- |
| [1. Síntese & Área Zero-DSP (Cyclone IV)](#sintese-cyclone-iv) | Matriz de silício e recursos | Hardware e FPGAs |
| [2. Arquitetura Modular: T-Link & Operador MEEC / M*](#arquitetura-meec) | Núcleo matemático e Redutor Zonotópico | Casos de Uso e Esquemáticos |
| [3. Bancada Real Cyclone IV](#bancada-cyclone-iv) | SPI Inter-FPGA, I2C e PWM (`tz-02` / `tz-03`) | Casos de Uso e Esquemáticos |
| [4. Drivers & API em C (SPI / Avalon)](#drivers-c) | Integração com `tz_sys_002_riscv` e MCUs | Fluxo de Integração / Casos de Uso |
| [5. Portabilidade RTL (Artix-7 & iCE40)](#portabilidade-rtl) | Migração *vendor-agnostic* e constraints | Hardware e FPGAs |
| [6. Fluxo Quartus II / Quartus Prime](#fluxo-quartus) | Síntese, Fitter e bitstream Cyclone IV | Fluxo de Integração |
| [7. Simulação RTL (GHDL + EPWave)](#simulacao-epwave) | Testbenches e verificação `PASS` | Fluxo de Integração |
| [8. Golden Reference C/C++ & Notas HLS](#golden-reference-c) | Validação *bit-accurate* e comparativo HLS | Fluxo de Integração |

---

<a id="sintese-cyclone-iv"></a>
## 1. Relatório de Síntese & Área Zero-DSP (Cyclone IV)

Todos os 100 IP Cores da **Tusitec Silicon Library** seguem a arquitetura **Zero-DSP**: a lógica aritmética, filtragem (`tz-06-dsp`) e controle (`tz-03-ctl`) é sintetizada em elementos lógicos padrão (LEs/LUTs e registradores), sem travar o projeto em blocos DSP proprietários.

### Matriz de Dispositivos Validados em Bancada

| Dispositivo | Família | Capacidade Lógica | Status Tusitec | Escopo Validado |
| :--- | :--- | :--- | :--- | :--- |
| **`EP4CE6E22C8`** | Altera / Intel Cyclone IV | 6.272 LEs · 270 Kbits RAM | **Validado em Bancada** | Núcleo compacto, barramento T-Link, `tz-02-com` (SPI/I2C) e `tz-03-ctl` (PWM) |
| **`EP4CE10E22C8`** | Altera / Intel Cyclone IV | 10.320 LEs · 414 Kbits RAM | **Validado em Bancada** | Pipeline completo Operador MEEC / M*, Filtro Ergódico, Redutor Zonotópico Bitônico e `tz-08-sys` |

---

<a id="arquitetura-meec"></a>
## 2. Arquitetura Modular: Barramento T-Link, Operador MEEC / M* & Redutor Zonotópico

A biblioteca adota uma topologia modular unificada sobre o pacote **`tusitec_tlink_pkg`**, permitindo encadear periféricos das famílias `tz-01` a `tz-10` com os núcleos matemáticos avançados da Tusitec (**Operador MEEC / M\***, **Filtro de Tensão Ergódico** e **Redutor Zonotópico Bitônico**):

```text
[ Periféricos tz-02 / tz-04 ] ──► [ Barramento T-Link ] ──► [ Operador MEEC / M* ] ──► [ Redutor Zonotópico ] ──► [ Atuação tz-03 ]
      (SPI / I2C / ADC)             (tusitec_tlink_pkg)        (Núcleo Zero-DSP)          (Ordenação Bitônica)       (PWM / Motores)
```

* **Canais T-Link (`0x01` a `0x64`):** Endereçamento padronizado que simplifica a interconexão entre módulos de lógica, comunicação, DSP e aceleradores especializados (`tz-10-esp`).
* **Latência Determinística:** Cada bloco opera em pipeline síncrono, ideal para estimação de estados em tempo real e controle embarcado.

---

<a id="bancada-cyclone-iv"></a>
## 3. Bancada Real Cyclone IV — SPI Inter-FPGA, I2C (BME280) e PWM

A validação física da biblioteca é executada em bancada com duas placas **Cyclone IV (`EP4CE6` 6k LEs e `EP4CE10` 10k LEs)** integrando os módulos nativos da biblioteca:

* **Comunicação SPI Inter-FPGA:** Enlace mestre/escravo entre as placas usando **`tz_com_002_spi_master`** (`0x0C`) e **`tz_com_003_spi_slave`** (`0x0D`).
* **Aquisição de Sensores via I2C (BME280):** Leitura direta em hardware via **`tz_com_004_i2c_master`** (`0x0E`) e blocos de `tz-04-aqd`.
* **Controle de Potência e Robótica:** Acionamento de ponte-H e motores DC integrando **`tz_ctl_001_pwm`** (`0x15`), **`tz_ctl_003_dead_time`** (`0x17`) e **`tz_ctl_004_dc_motor`** (`0x18`).

---

<a id="drivers-c"></a>
## 4. Driver / API em C (SPI / Avalon) — Integração Software-Hardware

Para sistemas híbridos (Hardware RTL + Firmware), os IP Cores T-Link podem ser controlados por uma camada leve em **C (`.h` / `.c`)** utilizando as pontes de barramento da família **`tz-08-sys`**:

* **Soft-Cores internos:** Integração direta via **`tz_sys_001_softcore`** (`0x47`), **`tz_sys_002_riscv`** (`0x48`), **`tz_sys_005_axi4_lite`** (`0x4B`), **`tz_sys_006_avalon`** (`0x4C`) ou **`tz_sys_007_wishbone`** (`0x4D`).
* **Microcontroladores externos:** Comunicação via SPI/UART a partir de **STM32**, **ESP32** ou **PIC18F4550** falando com `tz_com_003_spi_slave` ou `tz_com_001_uart`.

```c
/* Exemplo de assinatura padrão da camada de controle em C (T-Link) */
#include <stdint.h>

typedef struct {
    uint8_t  tlink_channel; /* Ex.: 0x0C (SPI), 0x15 (PWM), 0x5B (Sensor Fusion) */
    int32_t  payload_q16;   /* Dado em ponto fixo Q16.16 */
    uint32_t status_flags;
} tusitec_tlink_frame_t;

int tusitec_tlink_write(void *bus_handle, const tusitec_tlink_frame_t *tx);
int tusitec_tlink_read(void *bus_handle, uint8_t channel, tusitec_tlink_frame_t *rx);
```

---

<a id="portabilidade-rtl"></a>
## 5. Portabilidade VHDL Puro (Alvos Artix-7 & Lattice iCE40)

Como os 100 módulos utilizam exclusivamente bibliotecas padrão IEEE (`ieee.std_logic_1164` e `ieee.numeric_std`) sem primitivas fechadas de fabricante, a migração entre silícios exige apenas a troca do arquivo de pinagem e restrições de clock (*constraints*):

| Fabricante | Dispositivo Alvo | Constraints | Status |
| :--- | :--- | :--- | :--- |
| **Altera / Intel** | Cyclone IV (`EP4CE6` / `EP4CE10`) | `.qsf` + `.sdc` | Validado em Bancada |
| **AMD / Xilinx** | Artix-7 (`XC7A35T`) | `.xdc` | RTL Portável (Zero-DSP) |
| **Lattice Semiconductor** | iCE40 (`iCE40UP5K`) | `.pcf` | RTL Portável (Zero-DSP) |

---

<a id="fluxo-quartus"></a>
## 6. Fluxo de Síntese no Intel Quartus II / Quartus Prime

1. Crie o projeto no Quartus selecionando **`EP4CE6E22C8`** ou **`EP4CE10E22C8`**.
2. Adicione o pacote de barramento **`tusitec_tlink_pkg`** e os arquivos `.vhd` da família desejada (`tz-01-log` a `tz-10-esp`).
3. Configure o padrão de compilação para **VHDL-2008** (ou conforme indicado no `README.md` individual do módulo).
4. Importe o arquivo de pinagem (`.qsf`) e restrições temporais (`.sdc`), execute *Analysis & Synthesis → Fitter → Assembler* e grave via USB-Blaster (`.sof` / `.jic`).

---

<a id="simulacao-epwave"></a>
## 7. Simulação e Verificação RTL (GHDL + EPWave)

Todos os 100 IP Cores possuem status **`PASS`** em simulação funcional via **GHDL**, com inspeção de formas de onda (`.vcd` / `.ghw`) no **EPWave** ou **GTKWave**:

```bash
# Exemplo de fluxo padrão GHDL para qualquer módulo da biblioteca
ghdl -a --std=08 tusitec_tlink_pkg.vhd tz-03-ctl/tz_ctl_001_pwm/*.vhd
ghdl -e --std=08 tb_tz_ctl_001_pwm
ghdl -r --std=08 tb_tz_ctl_001_pwm --vcd=wave.vcd --stop-time=100us
```

---

<a id="golden-reference-c"></a>
## 8. Validação Bit-Accurate (Golden Reference C/C++ & Notas HLS/oneAPI)

* **Golden Reference em C/C++ (Ponto Fixo):** Modelos comportamentais usados para gerar vetores de teste e validar bit a bit a precisão numérica dos módulos matemáticos e DSP (`tz-06-dsp`, `tz-10-esp` e Operador MEEC) antes da síntese.
* **VHDL Artesanal vs. HLS / Altera oneAPI (SYCL):** Ferramentas HLS/oneAPI são voltadas a FPGAs de grande porte (Arria, Stratix, Agilex) e **não oferecem suporte nativo à Cyclone IV**. A Tusitec padroniza seus IP Cores em **VHDL puro** para garantir **Zero-DSP**, previsibilidade de *timing* e portabilidade real para dispositivos de borda.

---

**TUSITEC LTDA** · Portal do Desenvolvedor: [tusitec.com.br](https://www.tusitec.com.br) · Contato técnico: `tusitec@tusitec.com.br`
