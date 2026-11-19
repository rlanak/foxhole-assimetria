[Português](CONTRIBUTING.pt-BR.md) · **English**

# Contributing

Thanks for helping! This database is only useful if the numbers can be trusted, so there are a few rules.

## Golden rules

1. **Every number needs a public source.** Accepted:
   - a [Foxhole Wiki](https://foxhole.wiki.gg) page;
   - official patch notes or devblogs on [foxholegame.com](https://www.foxholegame.com);
   - an in-game test described reproducibly (version, steps, result). A public video helps.
2. **No personal or group data.** Don't include player names or nicknames, regiment names, private Discord links, screenshots with visible names, or reports that identify a group's operations.
3. **Keep data and opinion apart.** Numbers go in the CSVs. Gameplay reports go in the analysis pages, marked as "community report", and never replace a number.
4. **Stay impartial.** Both factions are judged by the same criteria. If a claim favours one side, show the counterpoint when there is one.

## Fixing or adding data

1. Edit the right CSV in `data/`. Keep the columns, and always fill in `source`.
2. If the change affects a conclusion, update the matching page in `analysis/` (English) and, if you can, in `analise/` (Portuguese). If you can only do one language, say so in the pull request and someone will fill in the other.
3. Open a pull request saying what changed, where the data came from, and the game version.

Not comfortable with Git? Open an issue using the **Data correction / Correção de dado** template and someone will apply it for you.

## When a game update ships

1. Add the relevant changes to `data/balance-changes.csv`.
2. Update the affected numbers in the other CSVs.
3. Update the version and verification date in both READMEs.
4. If a verdict changes, update the conclusions (`analysis/08-conclusion.md` and `analise/08-conclusao.md`) and the summary tables in both READMEs.

## Format

- CSV: UTF-8, comma-separated, values containing commas wrapped in double quotes.
- Numbers use a decimal point (`7.22`) and no thousands separator.
- Faction: `Colonial`, `Warden` or `Both`.
- Item names stay exactly as in the game.
