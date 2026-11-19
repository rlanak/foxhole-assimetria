# CLAUDE.md

Context for Claude Code (and any AI assistant) working in this repository.

## What this project is

An open, community-driven database comparing the two Foxhole factions, **Colonials** and **Wardens**, to answer one question with numbers: *is the game's asymmetry balanced?* It covers infantry, armour, artillery, naval, air, logistics, war history and balance changes.

It is an unofficial fan project, not affiliated with Siege Camp. Licence: CC BY-SA 4.0.

**Game version currently covered:** Update 67 (1.67.10.2). **Data last verified:** 2026-11-17.

## Repository layout

```
README.md              English (primary language)
README.pt-BR.md        Portuguese
CONTRIBUTING.md        English contribution guide
CONTRIBUTING.pt-BR.md  Portuguese contribution guide
analysis/              English analysis, one page per layer (01–08)
analise/               Portuguese analysis, same pages, same numbering
data/                  CSV tables, English only, single source of truth
sources.md / fontes.md Sources consulted (EN / PT)
scripts/validate.py    Checks CSVs and internal links
.github/               Bilingual issue and PR templates
```

Page pairs (keep them in sync):

| English | Portuguese |
| --- | --- |
| analysis/01-war-history.md | analise/01-historico-guerras.md |
| analysis/02-infantry.md | analise/02-infantaria.md |
| analysis/03-armour.md | analise/03-blindados.md |
| analysis/04-artillery.md | analise/04-artilharia.md |
| analysis/05-naval.md | analise/05-naval.md |
| analysis/06-air.md | analise/06-aereo.md |
| analysis/07-logistics.md | analise/07-logistica.md |
| analysis/08-conclusion.md | analise/08-conclusao.md |

## Non-negotiable rules

1. **No personal or group data, ever.** No player names or nicknames, regiment names, Discord servers or links, screenshots with names, account names, or anecdotes that identify a specific group's operations. If a contributor's report contains such details, keep the general fact and drop the identifying part ("a group refuelled a Pegasus from a barge" → "the Pegasus can refuel from a barge carrying a fuel truck").
2. **Every number needs a public source.** Acceptable: the Foxhole Wiki (foxhole.wiki.gg), official patch notes or devblogs on foxholegame.com, or a reproducible in-game test (version, steps, result). Every CSV row has a `source` column; never leave it empty.
3. **Data and opinion stay separate.** Numbers live in `data/*.csv`. Gameplay impressions go in the analysis pages labelled "community report" / "relato da comunidade" and never replace a number.
4. **Impartiality.** Judge both factions by the same criteria. When a claim favours one side, check it skeptically and state the counterpoint if one exists. Distinguish a real imbalance (same cost, clearly worse result) from a doctrine difference (different role or trade-off).
5. **Don't invent numbers.** If a stat isn't on a public source, say it's unknown rather than estimating. Raw calculations (e.g. "about 3 Myrmidons to kill a Flood") are fine if they say "raw, before resistances".

## Languages

- **English is primary.** `README.md` and `CONTRIBUTING.md` are English; Portuguese lives in `*.pt-BR.md`, `analise/` and `fontes.md`.
- Any change to an analysis page must be made in **both** `analysis/` and `analise/`. Same for the two READMEs (summary table, version, verification date) and the two CONTRIBUTING files.
- Each bilingual page starts with a language switcher line, e.g. `[Português](README.pt-BR.md) · **English**`.
- **CSV tables are English only.** Do not create Portuguese copies of the data.
- Item names always stay exactly as in the game (English), in both languages.

## Writing style for analysis pages

- Open with a **Bottom line / Conclusão** sentence that states the answer and its key number.
- Comparison tables: Colonial column, Warden column, then a short verdict column.
- Short sentences, specific numbers with units, no adjectives where a number will do.
- End each page with a `Sources:` / `Fontes:` line linking every page the numbers came from.
- Numbers in prose: English uses `1,250` and `7.22`; Portuguese uses `1.250` and `7,22`. Inside CSVs always use `7.22` with no thousands separator.

## CSV conventions

- UTF-8, comma-separated, LF line endings, header row in English snake_case.
- Values containing commas are wrapped in double quotes; a literal quote is doubled (`"H-5 ""Hatchet"""`).
- `faction` is `Colonial`, `Warden` or `Both`.
- Booleans are `yes` / `no`.
- `data/small-arms.csv` has `faction_confirmed`: the wiki doesn't label factions on the small-arms tables, so faction was inferred from naming (Latin/Greek = Colonial, English/Gaelic = Warden). Set it to `yes` only after confirming on the item's own wiki page.

## Common workflows

### A new game update ships

1. Read the official release notes (and the dev branch notes, which sometimes contain changes not repeated later).
2. Add one row per relevant change to `data/balance-changes.csv` (newest first): update, faction, item, change, type (`buff`, `nerf`, `change`), source.
3. Update affected numbers in the other CSVs. Re-check the item's wiki page; the wiki can lag a hotfix behind.
4. Update the affected analysis pages in both languages.
5. If a verdict changes, update `analysis/08-conclusion.md`, `analise/08-conclusao.md` and the summary tables in both READMEs.
6. Bump "Game version covered" and "Data last verified" in both READMEs and in this file.
7. Run `python scripts/validate.py`.

### A war ends

Add a row to the top of `data/wars.csv` (winner is `Colonial`, `Warden`, `Stalemate` or `Ongoing`), then update the counts in `analysis/01-war-history.md`, `analise/01-historico-guerras.md` and the README summaries.

### Checking a community claim

Treat claims from players (including the maintainer) as hypotheses. Look up the numbers, then report in the relevant page what is confirmed, what is partly true, and what the data contradicts.

## Foxhole Wiki quirks

- Some page titles use typographic quotes, so URLs need them encoded: `Toxot-902_%E2%80%9CBlind_Silver%E2%80%9D`, `Daimon_aK-5_%E2%80%9CHarpy%E2%80%9D`, `Mergo-4_%E2%80%9CMyrmidon%E2%80%9D`, `AC-b_%E2%80%9CTrident%E2%80%9D`. Others use plain or no quotes: `O-75b_%22Ares%22`, `M925_Austringer_Man-O-War`, `Rinnspeir_Mk._I_Zealot`. If one form 404s, try the others.
- The general `Aircraft` page says transports can only take off from a runway, which is outdated for the V-5b Pegasus (it can land on and take off from water).
- Large pages (Tanks, Small Arms) are long; stats for one faction may appear far down the page.

## Open questions (good first contributions)

- Harpy rate of fire, needed for a DPS comparison with the Harbinger.
- Whether the Mercy's cranes can recover non-amphibious aircraft (Harbinger, Austringer) from the water.
- Faction confirmation for every row in `data/small-arms.csv` (`faction_confirmed = no`).
- Faction of the Storm Cannon, Tempest Cannon RA-2, Huber Lariat, Huber Exalt and 50-500 "Thunderbolt" (currently inferred from naming).
- Speeds for the tanks that have no `road_speed_ms` value yet.

## Before committing

- Run `python scripts/validate.py` (checks CSV column counts, required `source` values and internal Markdown links).
- Re-read the diff for any personal or group-identifying information.
- Keep commit messages in English, short and descriptive (e.g. `Update 68: add Harpy and Predator changes`).
