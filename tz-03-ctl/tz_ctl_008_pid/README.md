# IP Core: `tz_ctl_008_pid`

**Família:** `tz-03-ctl` — Controle e Automação  
**Arquitetura:** Padrão T-Link | Zero-DSP | VHDL-93/2008  
**Canal T-Link (ID):** `0x1C`  
**Validação Funcional:** `PASS (100% GHDL)`  
**Desenvolvedor:** Tusitec Ltda ([tusitec.com.br](https://tusitec.com.br))

---

## 1. Visão Geral
O módulo **`tz_ctl_008_pid`** integra a biblioteca de silício da **Tusitec**, projetado para síntese direta em FPGAs (como a família **Intel/Altera Cyclone IV**) sem dependência de blocos multiplicadores dedicados (*Zero-DSP*). A comunicação com o roteador central é realizada nativamente pelo protocolo **T-Link**.

## 2. Interface de Hardware (Pinout)

| Sinal / Porta | Direção | Tipo / Largura |
| :--- | :---: | :--- |
| `clk` | `IN` | `std_logic` |
| `rst_n` | `IN` | `std_logic` |
| `din` | `IN` | `std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0)` |
| `fb_in` | `IN` | `std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0)` |
| `ctrl_out` | `OUT` | `std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0)` |
| `tlink_tx` | `OUT` | `t_tlink_s2m` |
| `tlink_rx` | `IN` | `t_tlink_m2s` |

## 3. Declaração da Entidade VHDL

```vhdl
entity tz_ctl_008_pid is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        fb_in : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        ctrl_out : out std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;
```

## 4. Estrutura de Diretórios
* `rtl/tz_ctl_008_pid.vhd`: Implementação sintetizável do núcleo em VHDL.
* `tb/tb_tz_ctl_008_pid.vhd`: Testbench automatizado de verificação funcional para GHDL.

---
*Propriedade Intelectual de **Tusitec Ltda** — Engenharia e Pesquisa & Desenvolvimento.*
