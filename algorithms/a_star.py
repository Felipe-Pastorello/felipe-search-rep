import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        distancia = 0

        for i in range(9):
            valor = state.tiles[i]

            if valor != 0:
                linha_atual = i // 3
                coluna_atual = i % 3

                linha_objetivo = (valor - 1) // 3
                coluna_objetivo = (valor - 1) % 3

                distancia += abs(linha_atual - linha_objetivo)
                distancia += abs(coluna_atual - coluna_objetivo)

        return distancia

    def search(self, initial: State) -> SearchResult:
        fila = []
        contador = 0

        heapq.heappush(
            fila,
            (self.heuristic(initial), contador, initial)
        )

        visitados = {}

        resultado = SearchResult(
            solution=None,
            nodes_generated=1
        )

        resultado.max_frontier_size = 1

        while fila:

            _, _, atual = heapq.heappop(fila)

            if atual.tiles in visitados:
                if visitados[atual.tiles] <= atual.cost:
                    continue

            visitados[atual.tiles] = atual.cost

            if atual.is_goal:
                resultado.solution = atual
                resultado.depth = len(atual.path()) - 1
                return resultado

            resultado.nodes_expanded += 1

            for vizinho in atual.neighbors():

                if vizinho.tiles not in visitados or vizinho.cost < visitados[vizinho.tiles]:
                    contador += 1

                    custo_total = (
                            vizinho.cost + self.heuristic(vizinho)
                    )

                    heapq.heappush(
                        fila,
                        (custo_total, contador, vizinho)
                    )

                    resultado.nodes_generated += 1

            if len(fila) > resultado.max_frontier_size:
                resultado.max_frontier_size = len(fila)

        return resultado
