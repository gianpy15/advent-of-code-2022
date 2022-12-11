from pathlib import Path

import numpy as np

values = [20, 60, 100, 140, 180, 220]


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    commands = file_path.read_text().splitlines()
    return commands


def part_one(input_lines: list[str]) -> int:
    x = 1
    clock = 1
    values_ = []
    for input_line in input_lines:
        match input_line.split():
            case ["noop"]:
                clock += 1
            case ["addx", value]:
                clock += 1
                if clock in values:
                    values_.append(clock * x)
                clock += 1
                x += int(value)
        if clock in values:
            values_.append(clock * x)
    return sum(values_)


def draw(vals: list[list[str]], clock, start_sprite) -> list[list[str]]:
    print(clock)
    if clock in range(
        (clock // 40) * 40 + start_sprite, (clock // 40) * 40 + start_sprite + 3
    ):
        vals[clock] = "#"
    return vals


def part_two(input_lines: list[str]) -> int:
    x = 0
    clock = 0
    vals = np.array(["."] * 40 * 6, dtype=str)
    for input_line in input_lines:
        match input_line.split():
            case ["noop"]:
                draw(vals, clock, x)
                clock += 1
            case ["addx", value]:
                draw(vals, clock, x)
                clock += 1
                draw(vals, clock, x)
                clock += 1
                x += int(value)
    with (Path(__file__).parent / "output.txt").open("w") as fp:
        for line in vals.reshape((6, 40)):
            fp.write("".join(line) + "\n")
    print(vals.reshape((6, 40)))


if __name__ == "__main__":
    input_lines = read_input_lines()
    print(part_one(input_lines))
    print(part_two(input_lines))
