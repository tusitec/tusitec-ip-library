# IP Core: `tz_log_002_counter`

**Família:** `tz-01-log` — Lógica e Aritmética  
**Arquitetura:** Padrão T-Link | Zero-DSP | VHDL-93/2008  
**Canal T-Link (ID):** `0x02`  
**Validação Funcional:** `PASS (100% GHDL)`  
**Desenvolvedor:** Tusitec Ltda ([tusitec.com.br](https://tusitec.com.br))

---

## 1. Visão Geral
O módulo **`tz_log_002_counter`** integra a biblioteca de silício da **Tusitec**, projetado para síntese direta em FPGAs (como a família **Intel/Altera Cyclone IV**) sem dependência de blocos multiplicadores dedicados (*Zero-DSP*). A comunicação com o roteador central é realizada nativamente pelo protocolo **T-Link**.

## 2. Interface de Hardware (Pinout)

| Sinal / Porta | Direção | Tipo / Largura |
| :--- | :---: | :--- |
| `clk` | `IN` | `std_logic` |
| `rst_n` | `IN` | `std_logic` |
| `enable` | `IN` | `std_logic` |
| `clear` | `IN` | `std_logic` |
| `tlink_tx` | `OUT` | `t_tlink_s2m` |
| `tlink_rx` | `IN` | `t_tlink_m2s` |

## 3. Declaração da Entidade VHDL

```vhdl
entity tz_log_002_counter is
    port (
        clk         : in  std_logic;
        rst_n       : in  std_logic;
        
        -- INTERFACE FISICA DO IP
        enable : in std_logic;
        clear : in std_logic;
        
        -- INTERFACE T-LINK
        tlink_tx    : out t_tlink_s2m;
        tlink_rx    : in  t_tlink_m2s
    );
end entity;
```

## 4. Estrutura de Diretórios
* `rtl/tz_log_002_counter.vhd`: Implementação sintetizável do núcleo em VHDL.
* `tb/tb_tz_log_002_counter.vhd`: Testbench automatizado de verificação funcional para GHDL.

---
*Propriedade Intelectual de **Tusitec Ltda** — Engenharia e Pesquisa & Desenvolvimento.*
