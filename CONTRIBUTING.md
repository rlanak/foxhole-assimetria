# Como contribuir

Obrigado por ajudar! Esta base só funciona se os números forem confiáveis. Por isso há algumas regras.

## Regras de ouro

1. **Todo número precisa de fonte pública.** Vale:
   - página do [Foxhole Wiki](https://foxhole.wiki.gg);
   - patch notes ou devblog oficial em [foxholegame.com](https://www.foxholegame.com);
   - teste no jogo descrito de forma reproduzível (versão, passo a passo, resultado). Vídeo público ajuda.
2. **Nada de dados pessoais ou de grupos.** Não inclua nomes ou nicks de jogadores, nomes de regimentos, links de Discord privado, prints com nomes visíveis ou relatos que identifiquem operações de um grupo.
3. **Separe dado de opinião.** Números vão nos CSVs. Relatos de jogo entram nos textos de `analise/` marcados como "relato da comunidade" e nunca substituem um número.
4. **Seja isento.** A análise compara as duas facções com o mesmo critério. Se uma afirmação favorece um lado, mostre também o contraponto quando ele existir.

## Corrigir ou adicionar um dado

1. Edite o CSV certo em `dados/`. Mantenha as colunas e a coluna `fonte` preenchida.
2. Se a mudança altera uma conclusão, atualize também a página correspondente em `analise/`.
3. Abra um pull request dizendo o que mudou, de onde veio o dado e a versão do jogo.

Não sabe usar Git? Abra uma *issue* com o modelo **Correção de dado** e alguém aplica para você.

## Novo update do jogo

Quando sair um patch:

1. Adicione as mudanças relevantes em `dados/mudancas-balanceamento.csv`.
2. Atualize os números afetados nos outros CSVs.
3. Atualize a versão e a data de verificação no `README.md`.
4. Se mudar algum veredito, ajuste `analise/08-conclusao.md` e a tabela de resumo do README.

## Formato

- CSV: UTF-8, separador vírgula, texto com vírgula entre aspas duplas.
- Números com ponto decimal (`7.22`), sem separador de milhar.
- Facção: `Colonial`, `Warden` ou `Ambas`.
- Idioma: português. Nomes de itens ficam como no jogo, em inglês.
