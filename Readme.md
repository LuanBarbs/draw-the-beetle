# Problema Implementado: Desenhar o Besouro Com o Dado

## Descrição

- Cada posição do dado desenha uma partedo besouro.
- O jogador que completar o desenho ganha o jogo.
- As posições do dado com o desenho são:
  - 1: desenharo corpo (1 vez)
  - 2: desenhara cabeça (1 vez)
  - 3: desenhara perna (6 vezes)
  - 4: desenharo olho (2 vezes)
  - 5: desenhara antena (2 vezes)
  - 6: desenharo rabo (1 vez).
- Temos que o corpo precisa ser o primeiro a ser desenhado, porque todas as outras partes se conectam ao corpo (se sair outras peças antes, nada é desenhado).
- O olho e antena só podem ser desenhados depois que a cabeça já tiver sido desenhada.
- E os desenhos das peças é limitado pelo número de vezesque pode ser aplicado.
  
## Exemplo
Ver exemplo no vídeo: [Conheça 3 Divertidos Jogos de Dados](https://www.youtube.com/watch?v=5hz3vsVtX7E&t=217s) (3o jogo).

## Buscas Implementados
- Buca Minimax;
- Busca Poda Alfa-Beta.

## Estrutura