[Português](README.pt-BR.md) · **English**

# Foxhole — Faction Asymmetry & Balance

An open, community-driven database comparing **Colonials** and **Wardens** in Foxhole: equipment, vehicles, ships, aircraft, war history and balance changes.

The goal is to answer one question with numbers instead of impressions: **is the game's asymmetry actually balanced?**

> Unofficial fan project, not affiliated with Siege Camp. Foxhole and all item names are trademarks of Siege Camp.

**Game version covered:** Update 67 (1.67.10.2) · **Data last verified:** 2026-11-17

---

## Current verdict (summary)

| Layer | Who comes out ahead | Size of the gap |
| --- | --- | --- |
| Infantry | Colonial (slightly) | Small |
| Armour (excluding super tanks) | Even: Colonials on HP, Wardens on speed and anti-infantry weapons | Small |
| Super tank | Warden (Predator > Ares) | Large |
| Artillery | Even, different philosophies | Small |
| Naval (surface) | Colonial (slightly) | Small to medium |
| Submarines | Depends on doctrine: Nakki for ambush, Trident for endurance | Medium |
| Air | Warden on fighters and anti-ship; Colonial on transport (amphibious Pegasus) | Medium |
| Aircraft carriers | Warden (crane recovery, instant launch) | Medium |
| Logistics | Even (symmetric) | Minimal |
| War results (2023–2026) | Wardens 24 × 16 Colonials; since the LIVE shard merge, 4 × 2 Colonials | — |

The full layer-by-layer analysis is in [`analysis/`](analysis/).

## Layout

```
analysis/              Analysis in English, one page per game layer
analise/               The same analysis in Portuguese
data/                  CSV tables (single source of truth)
sources.md             Every source consulted
CONTRIBUTING.md        How to fix a number or propose analysis
```

### Tables in `data/`

| File | Contents |
| --- | --- |
| [`wars.csv`](data/wars.csv) | Wars 100–142: dates, length, winner, game version |
| [`tanks.csv`](data/tanks.csv) | Every tank by faction: class, HP, armament, cost |
| [`aircraft.csv`](data/aircraft.csv) | Aircraft by faction: role, HP, speed, armament, endurance |
| [`ships.csv`](data/ships.csv) | Large and small ships by faction |
| [`small-arms.csv`](data/small-arms.csv) | Infantry weapons: damage, rate of fire, range, magazine |
| [`field-guns.csv`](data/field-guns.csv) | Towed field weapons by faction |
| [`balance-changes.csv`](data/balance-changes.csv) | Relevant nerfs and buffs by update |

Every CSV is UTF-8, comma-separated, and has a `source` column linking to where each number came from.

## Contributing

Found a wrong, outdated or missing number? Open an issue or a pull request. The rules are in [CONTRIBUTING.md](CONTRIBUTING.md). In short:

1. **Every number needs a public source** (wiki, official patch notes, or a reproducible in-game test).
2. **No personal data**: no player names, regiment names, private Discords or screenshots with names.
3. **Keep opinion apart from data**: gameplay reports go in as "community report", never as numbers.

Contributions in English or Portuguese are both welcome.

## License

Text and data under [CC BY-SA 4.0](LICENSE). Much of the data comes from the [Foxhole Wiki](https://foxhole.wiki.gg), which is also Creative Commons licensed; keep the attribution when reusing.
