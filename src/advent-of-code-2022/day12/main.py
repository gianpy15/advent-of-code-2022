from __future__ import annotations

import contextlib
import itertools
from pathlib import Path

import numpy as np
from dijkstar import Graph, NoPathError, find_path
from pydantic import BaseModel


class Level(BaseModel):
    value: str
    has_been_touched: bool = False

    @property
    def real_value(self) -> str:
        if self.value == "S":
            return "a"
        return "z" if self.value == "E" else self.value

    @property
    def ord_value(self) -> int:
        return ord(self.real_value)

    def __le__(self, other: Level):
        return self.real_value <= other.real_value

    def __eq__(self, other: Level | str) -> bool:
        if isinstance(other, Level):
            return self.value == other.value
        return self.value == other

    def can_move_to(self, other: Level):
        return other.ord_value - self.ord_value <= 1


def build_graph(input_lines: list[list[Level]]) -> Graph:
    graph = Graph()

    for x, y in itertools.product(range(len(input_lines)), range(len(input_lines[0]))):
        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            if (
                x + dx in range(len(input_lines))
                and y + dy in range(len(input_lines[0]))
                and input_lines[x][y].can_move_to(input_lines[x + dx][y + dy])
            ):
                graph.add_edge(
                    x * len(input_lines[0]) + y,
                    ((x + dx) * len(input_lines[0]) + y + dy),
                    1,
                )

    return graph


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    return [
        [Level(value=level) for level in line]
        for line in file_path.read_text().splitlines()
    ]


def part_one(input_lines: list[list[Level]]) -> int:
    start = tuple(np.argwhere(input_lines == "S")[0])
    start = start[0] * len(input_lines[0]) + start[1]
    end = tuple(np.argwhere(input_lines == "E")[0])
    end = end[0] * len(input_lines[0]) + end[1]
    graph = build_graph(input_lines)

    return find_path(graph, start, end).total_cost


def part_two(input_lines: list[list[Level]]) -> int:
    end = tuple(np.argwhere(input_lines == "E")[0])
    end = end[0] * len(input_lines[0]) + end[1]
    graph = build_graph(input_lines)

    starting_points = [
        x * len(input_lines[0]) + y
        for x, y in itertools.product(
            range(len(input_lines)), range(len(input_lines[0]))
        )
        if input_lines[x][y].real_value == "a"
    ]
    costs = []
    for start in starting_points:
        with contextlib.suppress(NoPathError):
            costs.append(find_path(graph, start, end).total_cost)
    return min(costs)


if __name__ == "__main__":
    input_lines = np.array(read_input_lines(), dtype=Level)
    print(part_one(input_lines))
    print(part_two(input_lines))
