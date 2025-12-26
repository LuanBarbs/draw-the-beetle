## MiniMax Clássico
O projeto implementa uma modelagem clássica de Inteligência Artificial para o jogo **Draw the Beetle**, utilizando **MiniMax** e **MiniMax com Poda Alfa-Beta**.

O fator aleatório do dado foi removido por discretização das ações, mantendo integralmente as regras do jogo original.

## Estado do Jogo
Cada jogador tem seu próprio besouro, representado por um vetor:

[state_corpo, state_cabeca, state_perna, state_olho, state_antena, state_rabo]

Estado inicial:
[0, 0, 0, 0, 0, 0]

Estado final:
[1, 1, 6, 2, 2, 1]

## Jogadores
- MAX: Jogador A
- MIN: Jogador B

Ambos jogam de forma alternada, tentando completar o próprio besouro primeiro.

## Ações Possíveis (sem dado)
Em cada turno, o jogador pode tentar uma das 6 ações:

| Ação | Peça    |
|------|---------|
| 0    | Corpo   |
| 1    | Cabeça  |
| 2    | Pernas  |
| 3    | Olhos   |
| 4    | Antenas |
| 5    | Rabo    |

## Regras de Transição
1. Corpo deve ser o primeiro
    - Nenhuma outra peça pode ser desenhada antes do corpo.
2. Cabeça depende do corpo
3. Olhos e antenas dependem da cabeça
4. Cada peça tem limite máximo
    - Corpo: 1
    - Cabeça: 1
    - Pernas: 6
    - Olhos: 2
    - Antenas: 2
    - Rabo: 1

Se uma ação viola regras → ação inválida, não gera sucessor.