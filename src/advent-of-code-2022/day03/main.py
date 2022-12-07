from pathlib import Path


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    return file_path.read_text().splitlines()


def get_ord(char: str) -> int:
    return ord(char) - 65 + 27 if char.isupper() else ord(char) - 96


def map_line(line) -> int:
    part1 = line[: len(line) // 2]
    part2 = line[len(line) // 2 :]

    print(line, " . ", part1, " . ", part2)

    for elem in part1:
        if elem in part2:
            return get_ord(elem)


def part_one(input_line: list[str]) -> int:
    return sum(map_line(line) for line in input_lines)


def find_common(lines: list[str]) -> str:
    for elem in lines[0]:
        if elem in lines[1] and elem in lines[2]:
            return elem


def part_two(input_line: list[str]) -> int:
    badges = [
        find_common(input_lines[i : i + 3]) for i in range(0, len(input_lines), 3)
    ]

    return sum(get_ord(x) for x in badges)


if __name__ == "__main__":
    input_lines = read_input_lines()
    print(part_one(input_lines))
    print(part_two(input_lines))
