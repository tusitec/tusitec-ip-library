# IP Core: `fusao-sensores`

**Família:** `tz-10-esp` — IP Cores Especializados  
**Arquitetura:** Padrão T-Link | Zero-DSP | VHDL-93/2008  
**Canal T-Link (ID):** `N/A`  
**Validação Funcional:** `PASS (100% GHDL)`  
**Desenvolvedor:** Tusitec Ltda ([tusitec.com.br](https://tusitec.com.br))

---

## 1. Visão Geral
O módulo **`fusao-sensores`** integra a biblioteca de silício da **Tusitec**, projetado para síntese direta em FPGAs (como a família **Intel/Altera Cyclone IV**) sem dependência de blocos multiplicadores dedicados (*Zero-DSP*). A comunicação com o roteador central é realizada nativamente pelo protocolo **T-Link**.

## 2. Interface de Hardware (Pinout)

| Sinal / Porta | Direção | Tipo / Largura |
| :--- | :---: | :--- |
| `clk`, `rst_n`, `din`, `tlink_tx`, `tlink_rx` | `IN/OUT` | Padrão T-Link |

## 3. Declaração da Entidade VHDL

```vhdl
-- Arquivo RTL: rtl/fusao-sensores.vhd
```

## 4. Estrutura de Diretórios
* `rtl/fusao-sensores.vhd`: Implementação sintetizável do núcleo em VHDL.
* `tb/tb_fusao-sensores.vhd`: Testbench automatizado de verificação funcional para GHDL.

---
*Propriedade Intelectual de **Tusitec Ltda** — Engenharia e Pesquisa & Desenvolvimento.*
