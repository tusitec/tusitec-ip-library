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

