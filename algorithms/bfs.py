from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:

        fila = deque([initial])
        visitados = {initial}

        resultado = SearchResult(
            solution=None,
            nodes_generated=1
        )

        resultado.max_frontier_size = 1

        while fila:

            atual = fila.popleft()

            if atual.is_goal:
                resultado.solution = atual
                resultado.depth = len(atual.path()) - 1
                return resultado

            resultado.nodes_expanded += 1

            for vizinho in atual.neighbors():

                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

                    resultado.nodes_generated += 1

            if len(fila) > resultado.max_frontier_size:
                resultado.max_frontier_size = len(fila)

        return resultado
