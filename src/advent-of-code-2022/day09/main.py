from __future__ import annotations
from pathlib import Path
from pydantic import BaseModel
import numpy as np

class Movement(BaseModel):
    direction: str
    steps: int

class Point(BaseModel):
    name: str
    pos_x: int = 0
    pos_y: int = 0
    tail: Point | None = None
    visited: set[tuple[int, int]] = {(0, 0)}

    @property
    def length(self) -> int:
        return 1 + self.tail.length if self.tail else 1
        

    def move(self, direction: Movement):
        for _ in range(direction.steps):
            match direction.direction:
                case "U":
                    self.pos_y += 1
                case "D":
                    self.pos_y -= 1
                case "L":
                    self.pos_x -= 1
                case "R":
                    self.pos_x += 1
            self.tail.update(self)

    def update(self, head: Point):
        dx = self.pos_x - head.pos_x
        dy = self.pos_y - head.pos_y
        if dx == -2:
            self.pos_x += 1
            if dy != 0:
                self.pos_y -= np.sign(dy)
        elif dx == 2:
            self.pos_x -= 1
            if dy != 0:
                self.pos_y -= np.sign(dy)
        elif dy == 2:
            self.pos_y -= 1
            if dx != 0:
                self.pos_x -= np.sign(dx)
        elif dy == -2:
            self.pos_y += 1
            if dx != 0:
                self.pos_x -= np.sign(dx)

        self.visited.add((self.pos_x, self.pos_y))
        if self.tail:
            self.tail.update(self)

    def plot(self):
        mappa = np.ones((1000, 1000), dtype=str)
        mappa[mappa=="1"] = "."
        for x, y in self.visited:
            mappa[y + 500, x + 500] = "#"
        
        with (Path(__file__).parent / "output.txt").open("w") as fp:
            for line in mappa:
                fp.write("".join(line) + "\n")
        

def read_input_lines() -> list[Movement]:
    file_path = Path(__file__).parent / "input.txt"
    return [Movement(**dict(zip(["direction", "steps"], mov.split()))) for mov in file_path.read_text().splitlines()]


def part_one(movements: list[Movement]) -> int:
    tail = Point(name="tail")
    head = Point(name="head", tail=tail)
    for movement in movements:
        head.move(movement)
    return len(tail.visited)



def part_two(movements: list[Movement]) -> int:
    curr_tail = Point(name=1)
    head = Point(name="head", tail=curr_tail)
    for i in range(8):
        tail = Point(name=i + 2)
        curr_tail.tail = tail
        curr_tail = tail
    for movement in movements:
        head.move(movement)
    
    while head.tail:
        head = head.tail
    head.plot()
    return len(head.visited)


if __name__ == "__main__":
    input_lines = read_input_lines()
    print(part_one(input_lines))
    print(part_two(input_lines))
