# Problema: Desenhar o Besouro Com o Dado

## Descrição

- Cada posição do dado desenha uma partedo besouro.
- O jogador que completar o desenho ganha o jogo.
- As posições do dado com o desenho são:
  - 1: desenhar o corpo (1 vez)
  - 2: desenhar a cabeça (1 vez)
  - 3: desenhar a perna (6 vezes)
  - 4: desenhar o olho (2 vezes)
  - 5: desenhar a antena (2 vezes)
  - 6: desenhar o rabo (1 vez).
- Temos que o corpo precisa ser o primeiro a ser desenhado, porque todas as outras partes se conectam ao corpo (se sair outras peças antes, nada é desenhado).
- O olho e antena só podem ser desenhados depois que a cabeça já tiver sido desenhada.
- E os desenhos das peças é limitado pelo número de vezes que pode ser aplicado.
  
## Exemplo
Ver exemplo no vídeo: [Conheça 3 Divertidos Jogos de Dados](https://www.youtube.com/watch?v=5hz3vsVtX7E&t=217s) (3o jogo).

## Jogo Estocástico de Soma Zero
O projeto implementa o jogo **Desenha o Besouro com o Dado** como um **problema clássico de Inteligência Artificial**, modelado como um **jogo estocástico de soma zero**, utilizando:

- MiniMax
- MiniMax com Poda Alfa-Beta
- Nós de Chance (dado)

O objetivo não é jogar interativamente, mas **encontrar políticas ótimas** para completar o besouro no menor número esperado de jogadas.

## Estado do Jogo
O estado é representado por um vetor:

[corpo, cabeça, pernas, olhos, antenas, rabo]

- Estado inicial: `[0, 0, 0, 0, 0, 0]`
- Estado final: `[1, 1, 6, 2, 2, 1]`

## O Dado
O dado é modelado como um **nó de chance**, com 6 resultados equiprováveis:

| Valor | Peça     |
|------:|----------|
| 1     | Corpo    |
| 2     | Cabeça   |
| 3     | Perna    |
| 4     | Olho     |
| 5     | Antena   |
| 6     | Rabo     |

## Algoritmos

- MiniMax Estocástico (Expectiminimax)
- MiniMax com Poda Alfa-Beta Parcial

## Estrutura
```
draw-the-beetle/
│
├── README.md
├── ABSTRACT.md
├── beetle_game.py
├── minimax.py
├── heuristics.py
├── tree_visualizer.py
└── main.py
```

## Como Jogar
No terminal, apenas execute:
```bash
python main.py

py main.py
```
Isso iniciará o jogo.

## Referências
- Russell & Norvig — Artificial Intelligence: A Modern Approach
- Pearl, J. — Heuristics: Intelligent Search Strategies
- Michie, D. — Game-playing and Problem-solving