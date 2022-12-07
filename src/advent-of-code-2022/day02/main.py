from pathlib import Path

outcomes = {
    ("A", "X"): 1 + 3,
    ("A", "Y"): 2 + 6,
    ("A", "Z"): 3 + 0,
    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,
    ("C", "X"): 1 + 6,
    ("C", "Y"): 2 + 0,
    ("C", "Z"): 3 + 3,
}

outcomes_2 = {
    ("A", "X"): 3 + 0,
    ("A", "Y"): 1 + 3,
    ("A", "Z"): 2 + 6,
    ("B", "X"): 1 + 0,
    ("B", "Y"): 2 + 3,
    ("B", "Z"): 3 + 6,
    ("C", "X"): 2 + 0,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 1 + 6,
}


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    return file_path.read_text().splitlines()


def part_one(input_lines) -> int:
    return sum(outcomes[tuple(line.split(" "))] for line in input_lines)


def part_two(input_lines: list[str]) -> int:
    return sum(outcomes_2[tuple(line.split(" "))] for line in input_lines)


if __name__ == "__main__":
    input_lines = read_input_lines()
    p1 = part_one(input_lines)
    p2 = part_two(input_lines)
    print(p1, p2)
