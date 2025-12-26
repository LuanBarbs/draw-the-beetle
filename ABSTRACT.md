# Resumo da Implementação

## Projeto
Este trabalho modela o jogo tradicional "Desenha o Besouro com o Dado" como um problema de decisão sequencial sob incerteza. Diferentemente de abordagens determinísticas, o jogo é tratado como um **processo estocástico**, no qual cada jogada depende do lançamento de um dado justo.

O estado do jogo é representado por um vetor discreto que contabiliza as partes do besouro já desenhadas. As transições de estado são condicionadas às regras estruturais do jogo, como dependências hierárquicas entre as peças.

Para resolver o problema, são implementados os algoritmos **Expectiminimax** e **Expectiminimax com poda Alfa-Beta**, permitindo comparar desempenho e qualidade da solução. Uma função heurística baseada em progressão estrutural ponderada é utilizada para avaliação de estados não terminais.

O estudo demonstra como jogos originalmente baseados em sorte podem ser formalmente analisados por técnicas clássicas de Inteligência Artificial.

## Regras do Jogo — Transições de Estado

### Dependências Estruturais
- Corpo:
  - Pode ser desenhado apenas uma vez
  - Não depende de nenhuma outra peça

- Cabeça:
  - Requer corpo
  - Apenas uma vez

- Perna:
  - Requer corpo
  - Até 6 vezes

- Olho:
  - Requer cabeça
  - Até 2 vezes

- Antena:
  - Requer cabeça
  - Até 2 vezes

- Rabo:
  - Requer corpo
  - Apenas uma vez

### Regra do Dado
Em cada jogada:
1. O dado é lançado (1 a 6)
2. A peça correspondente **só é adicionada se respeitar as regras**
3. Caso contrário, o estado permanece inalterado

## Heurística
Heurísticas baseadas em desbloqueio estrutural são comuns em jogos construtivos (Pearl, 1984). Corpo e cabeça recebem maior peso por habilitarem futuras ações.

## Observação
A poda Alfa-Beta não é totalmente eficaz em nós de chance, mas ainda reduz cálculo em práticas reais.
Memoization é padrão em jogos estocásticos (Russell & Norvig, Cap. 5) para evitar recomputação de estados equivalentes.