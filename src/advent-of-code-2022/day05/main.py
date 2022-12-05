from pathlib import Path
from pydantic import BaseModel

class Movement(BaseModel):
    move: str
    movements: int
    from_ : str
    start: int
    to: str
    end: int


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    lines = file_path.read_text().splitlines()
    stacks = [[] for _ in range(9)]
    movements = []
    map_ = []
    has_read_map = False
    for line in lines:
        if line != "" and not has_read_map:
            map_.append(line)
        elif line == "":
            has_read_map = True
        else:
            movements.append(Movement(**dict(zip(["move", "movements", "from_", "start", "to", "end"], line.split(' ')))))

    for line in map_[:-1]:
        for idx in range(0, len(map_[0]), 4):
            message = line[idx + 1]
            if message != " ":
                stacks[idx // 4].append(message)

    return [x[::-1] for x in stacks], movements


def part_one(stacks: list[list[str]], movements: list[Movement]) -> str:
    for movement in movements:
        for _ in range(movement.movements):
            element = stacks[movement.start - 1].pop()
            stacks[movement.end - 1].append(element)
    return "".join([x[-1] for x in stacks])

def part_two(stacks: list[list[str]], movements: list[Movement]) -> str:
    for movement in movements:
        elements = stacks[movement.start - 1][-movement.movements:]
        stacks[movement.start - 1] = stacks[movement.start - 1][:-movement.movements]
        stacks[movement.end - 1] += elements
    return "".join([x[-1] for x in stacks])



if __name__ == "__main__":
    stacks, movements = read_input_lines()
    # print(part_one(stacks, movements))
    print(part_two(stacks, movements))
