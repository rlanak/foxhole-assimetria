[Português](../analise/05-naval.md) · **English**

# Naval

**Bottom line:** at equal cost, Colonial ships have more HP in 5 of 9 paired classes, versus 2 for the Wardens. The relevant exception is the submarine: the Warden Nakki is better for ambush.

| Class | Colonial | Warden | HP difference |
| --- | --- | --- | --- |
| Submarine | AC-b "Trident": 28,500 HP, 2 torpedo tubes + 120mm | Nakki: 21,275 HP, 2 torpedo tubes + twin 68mm | Colonial +34% |
| Destroyer / frigate | Conqueror: 46,200 HP, 2× twin 120mm, twin 68mm | Blacksteele: 41,400 HP, 2× 120mm, 2× 68mm, quad depth charges | Colonial +12% |
| Battleship | Titan: 85,960 HP, 2× triple 150mm, twin 120mm | Callahan: 85,960 HP, 3× twin 150mm, 2× twin 120mm, 4× 30mm | Even |
| Aircraft carrier | Poseidon: 78,050 HP | Mercy: 74,750 HP | Colonial +4% |
| Gunboat | Type C "Charon": 1,850 HP | Ronan Gunship: 1,650 HP | Colonial +12% |
| Gunship | Strider: 2,300 HP, 40mm + 30mm, 500 Basic | Rinnspeir Ornitier: 2,050 HP, twin RPG + 30mm, 450 Basic | Colonial +12% (costs more) |
| Infantry boat | K-81e "Sombre": 1,500 HP, 2 passengers | Ronan Fathomer: 1,750 HP, 6 passengers | Warden +17% |
| Siege boat | Type B "Lucian": 1,800 HP, missiles | Ronan Blackguard: 2,000 HP, 250mm mortar | Warden +11% |
| Landing ship | Interceptor PA-12: 2,250 HP | MacConmara Shorerunner: 2,250 HP | Even |

Full data in [`data/ships.csv`](../data/ships.csv).

## Battleships

The Titan fires 150mm at 27.3 rpm versus 18.8 for the Callahan. The Callahan makes up for it with twice the 120mm guns and four 30mm deck guns. The naval edge players feel in the field tends to come from coordination and geography more than stats.

## Trident vs Nakki

The Nakki is smaller, harder to identify on sonar and harder to hit with depth charges at shallow depth, and needs fewer crew. It's also faster submerged (8.7 vs 7.8 knots). Torpedoes are identical (3,512 HE, 8 carried, 30–150 m).

The Trident has 34% more HP, dives deeper (25 vs 20 m) and stays submerged almost twice as long (33 min 20 s vs 17 min 50 s). It can also seal large holes by itself with metal beams.

The Trident's 120mm is a surface weapon: 400 HE, 100–225 m, for finishing off a crippled ship or shelling the coast after the torpedoes are spent. For stealth ambushes the Nakki is better; for long, deep patrols the Trident is. The Nakki is a hunter, the Trident an endurance boat.

## Update 68 dev branch (preview, not live)

The dev branch adds a light submarine and a sub-hunting light boat for each faction. Their wiki pages exist but are marked as unreleased content and list no HP, so there is no verdict yet.

| | AF-e "Palaemon" (Colonial) | Hodari (Warden) | Reading |
| --- | --- | --- | --- |
| Armament | 6 torpedo tubes, 12.7mm MG | 6 torpedo tubes, 12.7mm MG | Mirrored |
| Crew | 6 | 6 | Mirrored |
| Fuel | 200 L (44 min 27 s) | 250 L (55 min 33 s) | Warden +25% endurance |
| Speed | not listed | 12.4 knots (6.37 m/s) | Unknown |
| Cost | not listed | 125 Refined Materials | Unknown |
| HP | not listed | not listed | Unknown |

The patch notes describe the Palaemon as cheap and short-range, which matches its smaller fuel tank. Whether it is actually cheaper than the Hodari can't be checked until its cost is published.

- **Sub hunters.** The Type F "Abyss Trawler" (Colonial) and the Rinnspeir Reefward Patrol Boat (Warden) both carry a sonar array and a depth charge launcher, and neither is built for ship-to-ship combat. Only the Reefward has a wiki page so far: crew 3, 250 L fuel, 300 Basic Materials.
- **Model-8 "Kappa".** A new depth charge for light submarines, with a 5–30 m depth fuse. No faction is listed, so both sides should be able to use it.
- **Changes for both factions.** Ships get a throttle like aircraft. Vehicles can no longer anchor with enemy structures or vehicles nearby. Dive officers can see horizontal speed.
- **Naming.** On the dev branch the "Infantry Boat" class is renamed "Light Boat". The tables keep the live name until the update is released.

Sources: [Large Ships](https://foxhole.wiki.gg/wiki/Large_Ships), [Ships](https://foxhole.wiki.gg/wiki/Ships), [Nakki](https://foxhole.wiki.gg/wiki/Nakki), [Trident](https://foxhole.wiki.gg/wiki/AC-b_%E2%80%9CTrident%E2%80%9D), [Artillery](https://foxhole.wiki.gg/wiki/Artillery), [Update 68 dev branch](https://www.foxholegame.com/post/update-68-dev-branch-released), [Palaemon](https://foxhole.wiki.gg/wiki/AF-e_%22Palaemon%22), [Hodari](https://foxhole.wiki.gg/wiki/Hodari), [Reefward](https://foxhole.wiki.gg/wiki/Rinnspeir_Reefward_Patrol_Boat), [Kappa](https://foxhole.wiki.gg/wiki/Model-8_%E2%80%9CKappa%E2%80%9D)
