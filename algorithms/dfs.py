
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:

        pilha = [(initial, 0)]
        visitados = {initial}

        resultado = SearchResult(
            solution=None,
            nodes_generated=1
        )

        resultado.max_frontier_size = 1

        while pilha:

            atual, profundidade = pilha.pop()

            if atual.is_goal:
                resultado.solution = atual
                resultado.depth = profundidade
                return resultado

            if profundidade < self.depth_limit:

                resultado.nodes_expanded += 1

                for vizinho in atual.neighbors():

                    if vizinho not in visitados:

                        visitados.add(vizinho)
                        pilha.append((vizinho, profundidade + 1))

                        resultado.nodes_generated += 1

                if len(pilha) > resultado.max_frontier_size:
                    resultado.max_frontier_size = len(pilha)

        return resultado
