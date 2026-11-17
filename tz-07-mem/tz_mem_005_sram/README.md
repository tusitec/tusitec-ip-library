# IP Core: `tz_mem_005_sram`

**Família:** `tz-07-mem` — Memória e Armazenamento  
**Arquitetura:** Padrão T-Link | Zero-DSP | VHDL-93/2008  
**Canal T-Link (ID):** `0x41`  
**Validação Funcional:** `PASS (100% GHDL)`  
**Desenvolvedor:** Tusitec Ltda ([tusitec.com.br](https://tusitec.com.br))

---

## 1. Visão Geral
O módulo **`tz_mem_005_sram`** integra a biblioteca de silício da **Tusitec**, projetado para síntese direta em FPGAs (como a família **Intel/Altera Cyclone IV**) sem dependência de blocos multiplicadores dedicados (*Zero-DSP*). A comunicação com o roteador central é realizada nativamente pelo protocolo **T-Link**.

## 2. Interface de Hardware (Pinout)

| Sinal / Porta | Direção | Tipo / Largura |
| :--- | :---: | :--- |
| `clk` | `IN` | `std_logic` |
| `rst_n` | `IN` | `std_logic` |
| `din` | `IN` | `std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0)` |
| `sram_addr` | `OUT` | `std_logic_vector(18 downto 0)` |
| `sram_dq` | `INOUT` | `std_logic_vector(15 downto 0)` |
| `sram_ce_n` | `OUT` | `std_logic` |
| `sram_we_n` | `OUT` | `std_logic` |
| `sram_oe_n` | `OUT` | `std_logic` |
| `tlink_tx` | `OUT` | `t_tlink_s2m` |
| `tlink_rx` | `IN` | `t_tlink_m2s` |

## 3. Declaração da Entidade VHDL

```vhdl
entity tz_mem_005_sram is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        sram_addr : out std_logic_vector(18 downto 0);
        sram_dq : inout std_logic_vector(15 downto 0);
        sram_ce_n : out std_logic;
        sram_we_n : out std_logic;
        sram_oe_n : out std_logic;
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;
```

## 4. Estrutura de Diretórios
* `rtl/tz_mem_005_sram.vhd`: Implementação sintetizável do núcleo em VHDL.
* `tb/tb_tz_mem_005_sram.vhd`: Testbench automatizado de verificação funcional para GHDL.

---
*Propriedade Intelectual de **Tusitec Ltda** — Engenharia e Pesquisa & Desenvolvimento.*
