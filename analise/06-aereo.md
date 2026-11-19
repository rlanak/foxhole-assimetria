# Aéreo

**Conclusão:** os Wardens estão à frente nos caças e no ataque a navios. Pelo mesmo custo, o Harbinger tem mais vida e uma arma a mais que o Blind Silver. O Austringer ameaça navios grandes, e os Colonials não têm um equivalente dedicado. As vantagens Colonials são o Pegasus anfíbio e a capacidade do Poseidon, esta limitada na prática (ver porta-aviões).

| Papel | Colonial | Warden | Leitura |
| --- | --- | --- | --- |
| Caça padrão | Toxot-902 "Blind Silver": 5.500 HP, 22,75 m/s, 20 mm duplo (65–97) | Luminary Mk. II "Harbinger": 6.000 HP, 22 m/s, 20 mm duplo (65–97) + canhão 14,5 mm repetidor (225–337, 78/min) | Warden: mesmo custo, +500 HP e uma arma a mais |
| Caça anfíbio | — | Tulka I1.9 "White Raven": 5.750 HP, 18,5 m/s, 20 mm triplo (81–121, +25%), recarga de 7,5 s | Warden (único caça anfíbio) |
| Caça pesado | Daimon aK-5 "Harpy": 6.500 HP, 18,5 m/s, 4× rifle AT 14,5 mm (187–281, +25%), 20 mm defensivo, 8 min 41 s de autonomia | Sem equivalente; enfrenta o Harbinger | Harpy aguenta mais e voa mais tempo, mas é 16% mais lento e dá menos dano por tiro |
| Bombardeiro leve | Mergo-4 "Myrmidon": 5.500 HP, 2 bombas de 937 (perfurante) | M925 Austringer "Man-O-War": 7.000 HP, 2 torpedos de 1.038 (HE) | Assimétrico |
| Transporte | V-5b Pegasus: 7.000 HP, pousa e decola da água | Rinnspeir Mk. I "Zealot": 7.000 HP, só pista | Colonial |
| Bombardeiro pesado | V-1 Tzykalia: 10.000 HP, Raidbreaker | Tulka P4 "Welkinrive": 10.000 HP, Raidbreaker | Espelhados |
| Scouts (2 por lado) | Daedalus, Perdix | Herald, Emissary | Espelhados |

Dados completos em [`data/aircraft.csv`](../data/aircraft.csv).

## Caças

O Update 65 tirou o bônus de velocidade de projétil das metralhadoras do Blind Silver e do Harbinger. O White Raven ficou com +25%. Hoje os dois caças padrão têm a mesma 20 mm e o mesmo custo, mas o Harbinger soma o canhão de 14,5 mm e 500 HP. No papel o Blind Silver é pior, e a única vantagem dele é ser 0,75 m/s mais rápido.

## Harpy

O nerf veio antes do lançamento. Ainda no dev branch do Update 66, o bônus de velocidade dos 14,5 mm caiu de 50% para 25%, e a torreta de 20 mm ficou 30% mais lenta para girar. O Update 67 só aliviou a perda de controle quando danificado.

O Harpy ganha do Harbinger em vida (6.500 contra 6.000) e autonomia (8 min 41 s contra 6 min 58 s). Perde em velocidade (18,5 contra 22 m/s) e em dano por tiro (187–281 contra 225–337), e custa mais: 2 motores e 7 peças mecânicas contra 1 e 5. Em dogfight a velocidade decide quem escolhe a luta. O wiki não traz a cadência do Harpy, então a conta de DPS fica em aberto.

## Myrmidon × Austringer

O nerf do Myrmidon se confirma. No Update 64 a carga caiu de 4 para 2 bombas, e a salva passou a levar 6 s, com o objetivo declarado de reduzir a opressão dos aviões contra alvos em terra. Com 2 bombas de 937, um Myrmidon causa 1.874 de dano bruto por passada. Matar um Flood (5.100 HP) pede uns 3 Myrmidons, e um Predator (12.000 HP) uns 7, antes de resistências.

O Austringer leva 2 torpedos de 1.038, cada um com 15% de chance de abrir um vazamento grande. Com 2 Austringers (4 torpedos), a chance de pelo menos um vazamento grande é de cerca de 48%. Ele também não levou o nerf contra navio grande que a bomba Raidbreaker levou no Update 66 (resistência de 25% para 75%).

**Custo.** Na estação de montagem, o Myrmidon é mais caro: 40 PCM, 175 AM II e 50 AM III, contra 25, 100 e 20 do Austringer (AM I e Rare Alloys iguais). Só que o Austringer pede 3 motores pequenos contra 1 do Myrmidon. Pelo efeito, o Austringer é melhor negócio: tem 1.500 HP a mais e ameaça navios que custam de 12 a 20 segmentos de casco. A resposta Colonial a navios fica com o Myrmidon contra subsistemas e os mini torpedos do scout Perdix, nada dedicado.

## Pegasus × Zealot

Os dois têm a mesma vida, velocidade e armamento. A diferença está no combustível e na água:

| | V-5b Pegasus | Rinnspeir Mk. I Zealot |
| --- | --- | --- |
| Pousa e decola da água | Sim | Não, só pista |
| Tanque | 425 L | 250 L |
| Consumo | 62,4 L/min | 33,48 L/min |
| Autonomia | 6 min 49 s | 7 min 28 s |

O Zealot voa uns 40 s a mais por tanque, mas depende de pista para reabastecer. O Pegasus pode reabastecer em qualquer ponto de água com logística por perto (por exemplo, uma barcaça levando um caminhão-tanque), o que aumenta muito o alcance das operações de salto.

> A página geral [Aircraft](https://foxhole.wiki.gg/wiki/Aircraft) do wiki diz que transportes só decolam de pista, o que está desatualizado para o Pegasus.

## Porta-aviões

| | Poseidon (Colonial) | Mercy (Warden) |
| --- | --- | --- |
| Vida | 78.050 HP | 74.750 HP |
| Recuperação | Pouso no convés | Guindaste pega o avião na água e põe na catapulta |
| Lançamento | Monta a partir do estoque e sobe por plataforma | 3 catapultas, aviões prontos |
| Capacidade | Até 20 aviões no estoque | 3 (um por catapulta) |
| Reabastecimento | Galão na mão ou barcaça com caminhão-tanque | Galão na mão ou barcaça com caminhão-tanque (botão "refuel" na catapulta) |
| Reparo | Botão, 100 materiais básicos | Botão, 100 materiais básicos |
| Bônus | — | Menos consumo de combustível nos 3 primeiros minutos após lançar |

- **Mercy:** melhor para operação contínua com poucos aviões. O pouso é mais seguro e a decolagem imediata. O wiki só mostra o guindaste pegando White Raven e Herald (os Warden anfíbios), e não confirma se outros aviões podem esperar na água. Desde o Update 66, a defesa antiaérea mira aviões parados na água.
- **Poseidon:** a capacidade de 20 aviões vale menos na prática. A reserva de esquadrão do navio não protege o estoque, e qualquer aliado pode retirar os aviões guardados. Por isso o hangar interno é pouco usado. Permitir reserva nesse estoque seria uma correção simples.

Fontes: [Blind Silver](https://foxhole.wiki.gg/wiki/Toxot-902_%E2%80%9CBlind_Silver%E2%80%9D), [Harbinger](https://foxhole.wiki.gg/wiki/Luminary_Mk._II_Harbinger), [White Raven](https://foxhole.wiki.gg/wiki/Tulka_I1.9_White_Raven), [Harpy](https://foxhole.wiki.gg/wiki/Daimon_aK-5_%E2%80%9CHarpy%E2%80%9D), [Myrmidon](https://foxhole.wiki.gg/wiki/Mergo-4_%E2%80%9CMyrmidon%E2%80%9D), [Austringer](https://foxhole.wiki.gg/wiki/M925_Austringer_Man-O-War), [Pegasus](https://foxhole.wiki.gg/wiki/V-5b_Pegasus), [Zealot](https://foxhole.wiki.gg/wiki/Rinnspeir_Mk._I_Zealot), [Mercy](https://foxhole.wiki.gg/wiki/Mercy), [Poseidon](https://foxhole.wiki.gg/wiki/Poseidon), [Update 64](https://www.foxholegame.com/post/update-64-release-notes), [Update 65](https://www.foxholegame.com/post/update-65-release-notes), [Update 66 dev branch](https://www.foxholegame.com/post/update-66-dev-branch-released), [Update 66](https://www.foxholegame.com/post/update-66-release-notes)
