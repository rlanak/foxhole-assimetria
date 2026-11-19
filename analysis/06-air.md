[Português](../analise/06-aereo.md) · **English**

# Air

**Bottom line:** the Wardens are ahead on fighters and anti-ship strikes. At the same cost, the Harbinger has more HP and one more weapon than the Blind Silver. The Austringer threatens large ships, and the Colonials have no dedicated equivalent. Colonial strengths are the amphibious Pegasus and the Poseidon's capacity, the latter limited in practice (see carriers).

| Role | Colonial | Warden | Reading |
| --- | --- | --- | --- |
| Standard fighter | Toxot-902 "Blind Silver": 5,500 HP, 22.75 m/s, twin 20mm (65–97) | Luminary Mk. II "Harbinger": 6,000 HP, 22 m/s, twin 20mm (65–97) + repeating 14.5mm cannon (225–337, 78 rpm) | Warden: same cost, +500 HP and an extra weapon |
| Amphibious fighter | — | Tulka I1.9 "White Raven": 5,750 HP, 18.5 m/s, triple 20mm (81–121, +25%), 7.5 s reload | Warden (only amphibious fighter) |
| Heavy fighter | Daimon aK-5 "Harpy": 6,500 HP, 18.5 m/s, quad 14.5mm AT rifles (187–281, +25%), defensive 20mm, 8 min 41 s endurance | No equivalent; faces the Harbinger | Harpy is tougher and flies longer, but is 16% slower and deals less per hit |
| Light bomber | Mergo-4 "Myrmidon": 5,500 HP, 2 bombs of 937 (armour piercing) | M925 Austringer "Man-O-War": 7,000 HP, 2 torpedoes of 1,038 (HE) | Asymmetric |
| Transport | V-5b Pegasus: 7,000 HP, lands on and takes off from water | Rinnspeir Mk. I "Zealot": 7,000 HP, runway only | Colonial |
| Heavy bomber | V-1 Tzykalia: 10,000 HP, Raidbreaker | Tulka P4 "Welkinrive": 10,000 HP, Raidbreaker | Mirrored |
| Scouts (2 per side) | Daedalus, Perdix | Herald, Emissary | Mirrored |

Full data in [`data/aircraft.csv`](../data/aircraft.csv).

## Fighters

Update 65 removed the projectile velocity bonus from the Blind Silver's and Harbinger's machine guns. The White Raven kept +25%. Today both standard fighters have the same 20mm and the same cost, but the Harbinger adds the 14.5mm cannon and 500 HP. On paper the Blind Silver is worse; its only edge is being 0.75 m/s faster.

## Harpy

The nerf came before release. Still on the Update 66 dev branch, the 14.5mm velocity bonus dropped from 50% to 25%, and the 20mm turret's turn rate was cut by 30%. Update 67 only reduced how much damage affects its handling.

The Harpy beats the Harbinger on HP (6,500 vs 6,000) and endurance (8 min 41 s vs 6 min 58 s). It loses on speed (18.5 vs 22 m/s) and damage per hit (187–281 vs 225–337), and costs more: 2 engines and 7 mechanical parts vs 1 and 5. In a dogfight, speed decides who picks the fight. The wiki doesn't list the Harpy's rate of fire, so a DPS comparison is still open.

## Myrmidon vs Austringer

The Myrmidon nerf is confirmed. In Update 64 its payload went from 4 bombs to 2 and the drop now takes 6 s, with the stated goal of reducing how oppressive aircraft are against ground targets. With 2 bombs of 937, one Myrmidon deals 1,874 raw damage per pass. Killing a Flood (5,100 HP) takes roughly 3 Myrmidons, a Predator (12,000 HP) roughly 7, before resistances.

The Austringer carries 2 torpedoes of 1,038, each with a 15% chance of causing a Large Leak. With 2 Austringers (4 torpedoes), the chance of at least one Large Leak is about 48%. It also didn't receive the anti-large-ship nerf the Raidbreaker bomb got in Update 66 (large ship resistance from 25% to 75%).

**Cost.** At the assembly station the Myrmidon is more expensive: 40 PCM, 175 AM II and 50 AM III, versus 25, 100 and 20 for the Austringer (AM I and Rare Alloys equal). But the Austringer needs 3 small engines versus 1 for the Myrmidon. In terms of effect, the Austringer is the better deal: 1,500 more HP and it threatens ships costing 12 to 20 hull segments. The Colonial answer to ships is the Myrmidon against subsystems and the Perdix scout's mini torpedoes — nothing dedicated.

## Pegasus vs Zealot

Same HP, speed and armament. The difference is fuel and water:

| | V-5b Pegasus | Rinnspeir Mk. I Zealot |
| --- | --- | --- |
| Lands on / takes off from water | Yes | No, runway only |
| Fuel tank | 425 L | 250 L |
| Consumption | 62.4 L/min | 33.48 L/min |
| Endurance | 6 min 49 s | 7 min 28 s |

The Zealot flies about 40 s longer per tank but needs a runway to refuel. The Pegasus can refuel anywhere on water with logistics nearby (for example, a barge carrying a fuel truck), which greatly extends the reach of paradrop operations.

> The general [Aircraft](https://foxhole.wiki.gg/wiki/Aircraft) wiki page says transports can only take off from a runway, which is out of date for the Pegasus.

## Aircraft carriers

| | Poseidon (Colonial) | Mercy (Warden) |
| --- | --- | --- |
| HP | 78,050 | 74,750 |
| Recovery | Deck landing | Crane picks the aircraft up from the water and places it on a catapult |
| Launch | Assembled from storage and raised by platform | 3 catapults, aircraft ready to go |
| Capacity | Up to 20 aircraft in storage | 3 (one per catapult) |
| Refuelling | Fuel cans by hand or a barge with a fuel truck | Fuel cans by hand or a barge with a fuel truck ("refuel" button on the catapult) |
| Repair | Button, 100 Basic Materials | Button, 100 Basic Materials |
| Bonus | — | Reduced fuel consumption for the first 3 minutes after launch |

- **Mercy:** better for sustained operations with a few aircraft. Recovery is safer and launch is immediate. The wiki only shows the cranes lifting the White Raven and Herald (the amphibious Warden aircraft) and doesn't confirm whether other aircraft can wait on the water. Since Update 66, anti-air guns target aircraft floating on water.
- **Poseidon:** the 20-aircraft capacity is worth less in practice. The ship's squad reservation doesn't protect its storage, and any friendly player can withdraw stored aircraft, so the internal hangar sees little use. Allowing reservation of that storage would be a simple fix.

Sources: [Blind Silver](https://foxhole.wiki.gg/wiki/Toxot-902_%E2%80%9CBlind_Silver%E2%80%9D), [Harbinger](https://foxhole.wiki.gg/wiki/Luminary_Mk._II_Harbinger), [White Raven](https://foxhole.wiki.gg/wiki/Tulka_I1.9_White_Raven), [Harpy](https://foxhole.wiki.gg/wiki/Daimon_aK-5_%E2%80%9CHarpy%E2%80%9D), [Myrmidon](https://foxhole.wiki.gg/wiki/Mergo-4_%E2%80%9CMyrmidon%E2%80%9D), [Austringer](https://foxhole.wiki.gg/wiki/M925_Austringer_Man-O-War), [Pegasus](https://foxhole.wiki.gg/wiki/V-5b_Pegasus), [Zealot](https://foxhole.wiki.gg/wiki/Rinnspeir_Mk._I_Zealot), [Mercy](https://foxhole.wiki.gg/wiki/Mercy), [Poseidon](https://foxhole.wiki.gg/wiki/Poseidon), [Update 64](https://www.foxholegame.com/post/update-64-release-notes), [Update 65](https://www.foxholegame.com/post/update-65-release-notes), [Update 66 dev branch](https://www.foxholegame.com/post/update-66-dev-branch-released), [Update 66](https://www.foxholegame.com/post/update-66-release-notes)
