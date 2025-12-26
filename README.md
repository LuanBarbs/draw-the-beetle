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

## Buscas Implementados
- Buca Minimax;
- Busca Poda Alfa-Beta.

## Estrutura
```
draw-the-beetle/
│
├── README.md         # Instruções
├── ABSTRACT.md       # Resumo da Implementação
├── beetle_game.py    # Regras do jogo, Estado e Validação de Movimentos
├── ai.py             # Implementação do Minimax e Poda Alfa-Beta
└── main.py           # Loop principal (Menu e execução)
```

## Como Jogar
No terminal, apenas execute:
```bash
python main.py

py main.py
```
Isso iniciará o menu onde você pode selecionar se quer jogar contra a IA ou assistir duas IAs jogando.
