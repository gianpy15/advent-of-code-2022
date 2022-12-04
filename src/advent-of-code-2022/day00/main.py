from pathlib import Path


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    return file_path.read_text().splitlines()


def part_one(input_line: list[str]) -> int:
    pass

def part_two(input_line: list[str]) -> int:
    pass



if __name__ == "__main__":
    input_lines = read_input_lines()
    print(input_lines)
    print(part_one(input_lines))
    print(part_two(input_lines))
