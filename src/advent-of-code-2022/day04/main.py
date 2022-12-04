from pathlib import Path


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    lines = file_path.read_text().splitlines()
    return [[[int(x) for x in interval.split("-")] for interval in line.split(",")] for line in lines]

def map_lines(line):
    (ll, lr), (rl, rr) = line
    left = set(range(ll, lr+1))
    right = set(range(rl, rr+1))
    return left, right

def part_one(input_line: list[str]) -> int:
    count = [1 if left == left & right or right == left & right else 0 for left, right in input_lines]
    return sum(count)

def part_two(input_line: list[str]) -> int:
    count = [1 if left & right else 0 for left, right in input_lines]
    return sum(count)

if __name__ == "__main__":
    input_lines = list(map(map_lines, read_input_lines()))
    print(part_one(input_lines))
    print(part_two(input_lines))
