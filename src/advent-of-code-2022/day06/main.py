from pathlib import Path


def read_input_lines() -> str:
    file_path = Path(__file__).parent / "input.txt"
    return file_path.read_text()


def part_one(input_line: str) -> int:
    for i in range(len(input_line) - 4):
        window_end = i + 4
        if len(input_line[i:window_end]) == len(set(input_line[i:window_end])):
            return window_end


def part_two(input_line: list[str]) -> int:
    for i in range(len(input_line) - 14):
        window_end = i + 14
        if len(input_line[i:window_end]) == len(set(input_line[i:window_end])):
            return window_end


if __name__ == "__main__":
    input_line = read_input_lines()
    print(part_one(input_line))
    print(part_two(input_line))
