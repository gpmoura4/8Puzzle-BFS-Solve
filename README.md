# 8Puzzle-Problem-BFS

<img src="https://github.com/gpmoura4/8Puzzle-BFS-Solve/assets/78942968/d3ef0ab2-fe16-4e55-bb2c-a6a46eacce94" width="600px">

# 8Puzzle BFS Solver

Uma implementação em Python do clássico jogo de quebra-cabeça deslizante 8-puzzle com um solucionador automatizado usando o algoritmo de Busca em Largura (BFS).

## Descrição

Este projeto resolve o problema do 8-puzzle, um quebra-cabeças deslizante que consiste em uma grade 3x3 com oito peças numeradas (1-8) e um espaço vazio. O objetivo é organizar as peças em ordem numérica deslizando-as horizontal ou verticalmente para o espaço vazio.

O solucionador implementa o algoritmo de [Busca em Largura](https://developer.mozilla.org/pt-BR/docs/Web/API/BroadcastChannel) para encontrar o caminho de solução ótima de qualquer configuração inicial válida até o estado objetivo.

## Técnicas Interessantes

O código demonstra vários conceitos algorítmicos e de estruturas de dados:

- **Busca em Largura (BFS)**: Garante encontrar o caminho de solução mais curto explorando todos os estados na profundidade atual antes de avançar para o próximo nível
- **Busca no Espaço de Estados**: Representa as configurações do puzzle como nós em uma árvore de busca, onde cada movimento gera novos estados filhos
- **Processamento Baseado em Fila**: Utiliza [deque](https://docs.python.org/3/library/collections.html#collections.deque) do Python para operações FIFO eficientes na travessia BFS
- **Representação de Estados**: Converte grades 2D do puzzle em tuplas para comparação eficiente de estados e detecção de duplicatas
- **Reconstrução de Caminho**: Mantém relações pai-filho para reconstruir o caminho completo da solução do início ao objetivo

## Tecnologias e Bibliotecas

- **Python 3**: Linguagem de programação principal
- **collections.deque**: Fila de alta performance com duas extremidades para implementação BFS
- **Estruturas de Dados**: Listas e árvores para gerenciamento de estados e construção da árvore de busca

## Estrutura do Projeto

```
8Puzzle-BFS-Solve/
├── images/
└── 8puzzle.py
```

**images/**: Contém demonstrações visuais e exemplos do processo de solução do puzzle

## Funcionalidades

- Resolve qualquer configuração solucionável do 8-puzzle
- Encontra solução ótima (número mínimo de movimentos)
- Visualiza o caminho de solução passo a passo
- Trata estados de puzzle inválidos ou insolúveis
- Uso eficiente de memória através de desduplicação de estados

## Detalhes do Algoritmo

A abordagem BFS garante que a solução encontrada use o número mínimo de movimentos possível. O algoritmo:

1. Inicia com o estado inicial do puzzle
2. Gera todos os movimentos possíveis (cima, baixo, esquerda, direita)
3. Explora estados nível por nível até alcançar o objetivo
4. Rastreia estados visitados para evitar ciclos
5. Reconstrói o caminho ótimo do início ao objetivo

Esta implementação demonstra conceitos fundamentais em inteligência artificial e design de algoritmos, particularmente adequada para compreender problemas de busca em espaço de estados e algoritmos de busca de caminho ótimo.
