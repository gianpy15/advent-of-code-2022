# from functools import cached_property
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from pydantic import BaseModel


class Point(BaseModel):
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)


@dataclass
class Sand:
    rocks: dict[Point, int]
    grains: dict[Point, int] = field(default_factory=lambda: {})
    max_level: int = field(init=False)
    max_level_2: int = field(init=False)

    def __post_init__(self):
        self.max_level = max(r.y for r in self.rocks.keys())
        self.max_level_2 = self.max_level + 1

    def is_free(self, x, y):
        point = Point(x=x, y=y)
        return (point not in self.grains) and (point not in self.rocks)

    def add_grains_2(self) -> None:
        grain = Point(x=500, y=0)

        while True:
            if grain.y == self.max_level_2:
                # grain reached the base
                self.grains[grain] = 1
                grain = Point(x=500, y=0)
            elif self.is_free(grain.x, grain.y + 1):
                # down
                grain.y = grain.y + 1
            elif self.is_free(grain.x - 1, grain.y + 1):
                # down-left
                grain.x -= 1
                grain.y += 1
            elif self.is_free(grain.x + 1, grain.y + 1):
                # down-right
                grain.x += 1
                grain.y += 1
            elif grain.y == 0:
                # The last to be generated
                self.grains[grain] = 1
                break
            else:
                # add the grain in its final position
                self.grains[grain] = 1
                # make a new grain fall
                grain = Point(x=500, y=0)
    
    def add_grains_1(self) -> None:
        grain = Point(x=500, y=0)

        while True:
            if grain.y == self.max_level:
                # grain fall into void
                break
            elif self.is_free(grain.x, grain.y + 1):
                # down
                grain.y = grain.y + 1
            elif self.is_free(grain.x - 1, grain.y + 1):
                # down-left
                grain.x -= 1
                grain.y += 1
            elif self.is_free(grain.x + 1, grain.y + 1):
                # down-right
                grain.x += 1
                grain.y += 1
            else:
                # add the grain in its final position
                self.grains[grain] = 1
                # make a new grain fall
                grain = Point(x=500, y=0)


def read_input_lines() -> dict[Point, int]:
    file_path = Path(__file__).parent / "input.txt"
    paths = file_path.read_text().splitlines()
    rocks: dict[Point, int] = {}
    for path in paths:
        curr_x = None
        curr_y = None
        points = path.split(" -> ")
        for point in points:
            x, y = point.split(",")
            x, y = int(x), int(y)
            if curr_x is None:
                curr_x, curr_y = x, y
                rocks[Point(x=x, y=y)] = 1
            elif abs(curr_x - x) == 0:
                # y-movement
                for i in range(min(curr_y, y), max(curr_y, y) + 1):
                    rocks[Point(x=curr_x, y=i)] = 1
            else:
                # x-movement
                for i in range(min(curr_x, x), max(curr_x, x) + 1):
                    rocks[Point(x=i, y=curr_y)] = 1
            # update curr pos
            curr_x = x
            curr_y = y

    return rocks


def part_one(rocks: dict[Point, int]) -> int:
    sand = Sand(rocks=rocks)
    sand.add_grains_1()
    return len(sand.grains)


def part_two(rocks: dict[Point, int]) -> int:
    sand = Sand(rocks=rocks)
    sand.add_grains_2()
    return len(sand.grains)


if __name__ == "__main__":
    rocks = read_input_lines()
    print(part_one(rocks))
    print(part_two(rocks))
