from numpy.typing import NDArray
from sortedcollections import ValueSortedDict

from adventofcode.grid.grid import Grid


class Node:
    def __init__(
        self,
        position: NDArray,
        tentative_cost: int,
        heuristic_cost: int,
        predecessor: NDArray | None,
    ):
        self._position = position
        self._tentative_cost = tentative_cost
        self._heuristic_cost = heuristic_cost
        self._predecessor = predecessor

    @property
    def position(self) -> NDArray:
        return self._position

    @property
    def tentative_cost(self) -> int:
        return self._tentative_cost

    @property
    def heuristic_cost(self) -> int:
        return self._heuristic_cost

    @property
    def predecessor(self) -> NDArray | None:
        return self._predecessor


class AStar:
    def __init__(self, grid: Grid):
        self.open_list = ValueSortedDict(
            lambda node: node.tentative_cost + node.heuristic_cost
        )
        self.closed_list: dict[tuple, Node] = {}
        self.grid = grid

    def heuristic(self, pos: NDArray, finish: NDArray | None = None) -> int:
        return self.grid.heuristic(pos, finish)

    def expand_node(self, node: Node) -> None:
        neighbors = self.grid.expand_node(node.position)
        for neighbor in neighbors:
            if tuple(neighbor) in self.closed_list.keys():
                continue

            tentative_cost = node.tentative_cost + self.heuristic(
                node.position, neighbor
            )

            if not (tuple(neighbor) in self.open_list.keys()) or (
                tentative_cost < self.open_list[tuple(neighbor)].tentative_cost
            ):
                self.open_list[tuple(neighbor)] = Node(
                    position=neighbor,
                    tentative_cost=tentative_cost,
                    heuristic_cost=self.heuristic(node.position),
                    predecessor=node.position,
                )

    def search(self, start: NDArray):
        self.open_list.clear()
        self.closed_list.clear()
        current_node = Node(
            position=start,
            tentative_cost=0,
            heuristic_cost=self.heuristic(start),
            predecessor=None,
        )
        while not self.grid.is_finish(current_node.position):
            self.closed_list[tuple(current_node.position)] = current_node
            self.expand_node(current_node)
            _, current_node = self.open_list.popitem(0)

        path = []
        cost = current_node.tentative_cost
        while current_node.predecessor is not None:
            path.insert(0, current_node.position)
            current_node = self.closed_list[tuple(current_node.predecessor)]
        return path, cost
