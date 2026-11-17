# IP Core: `tz_com_009_eth_mac`

**Família:** `tz-02-com` — Comunicação e Protocolos  
**Arquitetura:** Padrão T-Link | Zero-DSP | VHDL-93/2008  
**Canal T-Link (ID):** `0x13`  
**Validação Funcional:** `PASS (100% GHDL)`  
**Desenvolvedor:** Tusitec Ltda ([tusitec.com.br](https://tusitec.com.br))

---

## 1. Visão Geral
O módulo **`tz_com_009_eth_mac`** integra a biblioteca de silício da **Tusitec**, projetado para síntese direta em FPGAs (como a família **Intel/Altera Cyclone IV**) sem dependência de blocos multiplicadores dedicados (*Zero-DSP*). A comunicação com o roteador central é realizada nativamente pelo protocolo **T-Link**.

## 2. Interface de Hardware (Pinout)

| Sinal / Porta | Direção | Tipo / Largura |
| :--- | :---: | :--- |
| `clk` | `IN` | `std_logic` |
| `rst_n` | `IN` | `std_logic` |
| `din` | `IN` | `std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0)` |
| `mdc` | `OUT` | `std_logic` |
| `mdio` | `INOUT` | `std_logic` |
| `rxd` | `IN` | `std_logic_vector(1 downto 0)` |
| `txd` | `OUT` | `std_logic_vector(1 downto 0)` |
| `tlink_tx` | `OUT` | `t_tlink_s2m` |
| `tlink_rx` | `IN` | `t_tlink_m2s` |

## 3. Declaração da Entidade VHDL

```vhdl
entity tz_com_009_eth_mac is
    port (
        clk      : in  std_logic;
        rst_n    : in  std_logic;
        din : in std_logic_vector(C_TLINK_DATA_WIDTH-1 downto 0);
        mdc : out std_logic;
        mdio : inout std_logic;
        rxd : in std_logic_vector(1 downto 0);
        txd : out std_logic_vector(1 downto 0);
        tlink_tx : out t_tlink_s2m;
        tlink_rx : in  t_tlink_m2s
    );
end entity;
```

## 4. Estrutura de Diretórios
* `rtl/tz_com_009_eth_mac.vhd`: Implementação sintetizável do núcleo em VHDL.
* `tb/tb_tz_com_009_eth_mac.vhd`: Testbench automatizado de verificação funcional para GHDL.

---
*Propriedade Intelectual de **Tusitec Ltda** — Engenharia e Pesquisa & Desenvolvimento.*
