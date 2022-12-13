from functools import cmp_to_key
from pathlib import Path


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    output = [[]]
    for line in file_path.read_text().splitlines():
        if line == "":
            output.append([])
        else:
            output[-1].append(eval(line))

    return output


def check_input(lists: tuple[list, list]) -> bool:
    left, right = lists
    for i in range(min(len(left), len(right))):
        left_elem = left[i]
        right_elem = right[i]
        if isinstance(left_elem, list):
            check = check_input(
                (
                    left_elem,
                    right_elem if isinstance(right_elem, list) else [right_elem],
                )
            )
            if check is None:
                continue
            return check
        if isinstance(right_elem, list):
            check = check_input(
                (left_elem if isinstance(left_elem, list) else [left_elem], right_elem)
            )
            if check is None:
                continue
            return check
        if right_elem < left_elem:
            return False
        if right_elem > left_elem:
            return True
        continue
    if len(left) < len(right):
        return True
    return False if len(left) > len(right) else None


def part_one(input_lines: list[list]) -> int:
    samples = [check_input(sample) for sample in input_lines]

    return sum(i + 1 for i in range(len(samples)) if samples[i])


def part_two(input_lines: list[str]) -> int:
    flat_list = [item for sublist in input_lines for item in sublist]
    flat_list.extend(([[6]], [[2]]))
    flat_list = sorted(
        flat_list, key=cmp_to_key(lambda x, y: -1 if check_input((x, y)) else 1)
    )
    return (flat_list.index([[6]]) + 1) * (flat_list.index([[2]]) + 1)


if __name__ == "__main__":
    input_lines = read_input_lines()
    print(part_one(input_lines))
    print(part_two(input_lines))
