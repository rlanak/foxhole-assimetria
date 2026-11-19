**Português** · [English](README.md)

# Foxhole — Assimetria e Balanceamento entre Facções

Base de dados aberta e comunitária para comparar **Colonials** e **Wardens** no Foxhole: equipamento, veículos, navios, aeronaves, histórico de guerras e mudanças de balanceamento.

O objetivo é responder com números, e não com impressão, à pergunta: **a assimetria do jogo está equilibrada?**

> Projeto de fãs, não oficial. Não tem relação com a Siege Camp. Foxhole e todos os nomes de itens são marcas da Siege Camp.

**Versão do jogo coberta:** Update 67 (1.67.10.2) · **Última verificação dos dados:** 2026-11-17

---

## Veredito atual (resumo)

| Camada | Quem leva | Tamanho da diferença |
| --- | --- | --- |
| Infantaria | Colonial (leve) | Pequeno |
| Blindados (sem super tanque) | Empate: Colonial em vida, Warden em velocidade e armas anti-infantaria | Pequeno |
| Super tanque | Warden (Predator > Ares) | Grande |
| Artilharia | Empate, filosofias diferentes | Pequeno |
| Naval (superfície) | Colonial (leve) | Pequeno a médio |
| Submarinos | Depende da doutrina: Nakki para emboscada, Trident para resistência | Médio |
| Aéreo | Warden nos caças e anti-navio; Colonial no transporte (Pegasus anfíbio) | Médio |
| Porta-aviões | Warden (pouso por guindaste, lançamento imediato) | Médio |
| Logística | Empate (simétrica) | Mínimo |
| Resultado das guerras (2023–2026) | Wardens 24 × 16 Colonials; desde a fusão LIVE, 4 × 2 Colonials | — |

A análise completa, camada por camada, está em [`analise/`](analise/).

## Estrutura

```
analise/               Análise em português, uma página por camada do jogo
analysis/              A mesma análise em inglês
data/                  Tabelas em CSV (em inglês, uma única fonte de dados)
fontes.md              Fontes consultadas
CONTRIBUTING.pt-BR.md  Como corrigir um dado ou propor uma análise
```

### Tabelas disponíveis em `data/`

As tabelas ficam só em inglês para não existirem duas versões dos mesmos números.

| Arquivo | Conteúdo |
| --- | --- |
| [`wars.csv`](data/wars.csv) | Guerras 100–142: datas, duração, vencedor, versão |
| [`tanks.csv`](data/tanks.csv) | Todos os tanques por facção: classe, HP, armamento, custo |
| [`aircraft.csv`](data/aircraft.csv) | Aeronaves por facção: papel, HP, velocidade, armamento, autonomia |
| [`ships.csv`](data/ships.csv) | Navios grandes e pequenos por facção |
| [`small-arms.csv`](data/small-arms.csv) | Armas de infantaria: dano, cadência, alcance, pente |
| [`field-guns.csv`](data/field-guns.csv) | Armas de campo rebocáveis por facção |
| [`balance-changes.csv`](data/balance-changes.csv) | Nerfs e buffs relevantes por update |

Todo CSV usa vírgula como separador, UTF-8, e tem uma coluna `source` com o link de onde o número veio.

## Como contribuir

Achou um número errado, desatualizado ou faltando? Abra uma *issue* ou um *pull request*. As regras estão no [CONTRIBUTING.pt-BR.md](CONTRIBUTING.pt-BR.md). Em resumo:

1. **Todo número precisa de fonte pública** (wiki, patch notes oficiais ou teste reproduzível descrito).
2. **Nada de dados pessoais**: sem nomes de jogadores, regimentos, Discords privados ou prints com nomes.
3. **Opinião vai separada de dado**: relatos de jogo entram como "relato da comunidade", nunca como número.

## Licença

Texto e dados sob [CC BY-SA 4.0](LICENSE). Boa parte dos números vem do [Foxhole Wiki](https://foxhole.wiki.gg), que também usa licença Creative Commons; mantenha a atribuição ao reutilizar.
