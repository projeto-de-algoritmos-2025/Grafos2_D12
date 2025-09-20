# Grafos 2 - LeetCode

**Número da Lista**: 2  
**Conteúdo da Disciplina**: FGA0124 - PROJETO DE ALGORITMOS - T01  


## Alunos


<div align = "center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/CarolinaBarb"><img style="border-radius: 95%;" src=./Documentos/assets/Carolina.jpg width="201"; alt="Carolina"/><br /><sub><b>Carolina Barbosa </b></sub></a><br/></td>
    <td align="center"><a href="https://github.com/JuliaSSouza"><img style="border-radius: 95%;" src=./Documentos/assets/Julia.png width="195"; alt=""/><br /><sub><b>Julia Sant'Anna</b></sub></a><br />
  </tr>
</table>


| Matrícula   | Aluno                             |
| ----------- | ---------------------------------- |
| 211030961 | Carolina Barbosa Brito           |
| 202044144  | Julia Sant'Anna de Souza      |
</div>

## Sobre 

## Exercício 1 - Path with Maximun Probability
### Descrição
Este problema envolve encontrar o caminho com a maior probabilidade de sucesso em um grafo não dirigido e ponderado, onde cada aresta tem uma probabilidade associada à sua travessia bem-sucedida. Dados um número de nós, uma lista de arestas e as probabilidades de sucesso para cada aresta, o objetivo é determinar a maior probabilidade de ir do nó inicial até o nó final. O problema pode ser resolvido utilizando uma variação do algoritmo de Dijkstra, adaptado para maximizar as probabilidades de sucesso ao invés de minimizar distâncias, explorando sempre o caminho com a maior probabilidade até alcançar o destino ou concluir que não há caminho possível.

- Dificuldade: Médio
- Link: https://leetcode.com/problems/path-with-maximum-probability/description/
- Solução: [Código](https://github.com/projeto-de-algoritmos-2025/Grafos2_D12/blob/main/PathMaxProb.py)

## Exercício 2 - Find Critical and Pseudo Critical Edges in Minimum Spanning Tree
### Descrição
Este problema envolve identificar as arestas críticas e pseudo-críticas em uma Árvore Geradora Mínima (MST) de um grafo não direcionado e ponderado. O objetivo é determinar quais arestas, se removidas, aumentam o peso do MST (arestas críticas) e quais podem aparecer em alguns MSTs, mas não em todos (arestas pseudo-críticas). A solução é baseada no algoritmo de Kruskal, utilizando a estrutura Union-Find para calcular o MST e verificar a inclusão ou exclusão de arestas, realizando múltiplos cálculos para determinar as arestas críticas e pseudo-críticas.

![](Documentos/screenshots/exercicio%202.png)

- Dificuldade: Difício
- Link: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/description/
- Solução: [Código](https://github.com/projeto-de-algoritmos-2025/Grafos2_D12/blob/main/FindCritical.cpp)


## Como rodar o projeto


## Apresentação 
[Vídeo]()

 
 
