# Resumo da Implementação

## Representação do Estado
Vetor de inteiros [0,0,0,0,0,0] para cada jogador.

## Transição
- Não usamos dados aleatórios.
- O jogador escolhe entre Adicionar peças ao seu besouro (respeitando a hierarquia Corpo > Cabeça > Antena) ou Remover peças do oponente (respeitando a hierarquia inversa Antena > Cabeça > Corpo).

## Algoritmo
- Minimax com Poda Alfa-Beta.
- A função is_terminal detecta a condição de vitória [1, 1, 6, 2, 2, 1].
- A função evaluate pondera as peças para guiar a IA quando ela não consegue enxergar até o fim do jogo.

## Desafios
- O principa desafio é que o jogo original do "Besouro" é puramente estocástico (baseado na sorte do dado) e o Minimax serve para jogos determinísticos de estratégia perfeita.
- Para que o algoritmo funcione, deve-se adicionar uma mecânica de "Ataque e Defesa". O jogo será transformado em uma Variação Tática, onde em vez de rolar um dado, o jogados escolhe qual peça adicionar (Criar) e qual peça remover do oponente (Sabotar).

## Definição de Regras e Estado

### Construção:
- Corpo: Sem dependência.
- Cabeça, Perna, Rabo: Exigem Corpo.
- Olho, Antena: Exigem Cabeça.

### Sabotagem (Remoção):
- Você só pode remover uma peça do oponente se ela não tiver "filhos".
- Ex: Não pode remover a Cabeça do oponente se ele tiver Olhos. Primeiro remova os Olhos.

## Heurística
Como a árvore de decisão pode ser profunda, é necessária uma função que avalie quão bom é um estado caso não cheguemos ao fim.
- Valor = (Minhas Peças Ponderadas) - (Peças do Oponente Ponderadas).
- Peso maior para Corpo e Cabeça, pois desbloqueiam outros movimentos.