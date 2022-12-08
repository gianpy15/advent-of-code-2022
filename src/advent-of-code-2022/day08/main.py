from pathlib import Path

import numpy as np


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    return np.array(
        [[int(x) for x in line] for line in file_path.read_text().splitlines()],
        dtype=np.int32,
    )


def build_visibility_map(input_line: np.ndarray) -> np.ndarray:
    rows, cols = np.shape(input_lines)
    visibility_map = np.zeros(shape=np.shape(input_line), dtype=np.int8)

    visibility_map[:, 0] = 1
    visibility_map[:, -1] = 1
    visibility_map[0, :] = 1
    visibility_map[-1, :] = 1

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # check left row
            if (input_line[row, :col] < input_line[row, col]).all():
                visibility_map[row, col] = 1

            # Check right row
            if (input_line[row, col + 1 :] < input_line[row, col]).all():
                visibility_map[row, col] = 1

            # Check up col
            if (input_line[:row, col] < input_line[row, col]).all():
                visibility_map[row, col] = 1

            # Check right row
            if (input_line[row + 1 :, col] < input_line[row, col]).all():
                visibility_map[row, col] = 1
    return visibility_map


def get_score(trees: np.ndarray, tree: int) -> int:
    curr_score = 0
    for x in trees:
        if x < tree:
            curr_score += 1
        else:
            return curr_score + 1
    return curr_score


def part_one(input_lines: np.ndarray) -> int:
    return np.sum(build_visibility_map(input_lines))


def part_two(input_lines: np.ndarray) -> int:
    tree_score = np.ones(shape=input_lines.shape, dtype=np.int32)
    rows, cols = input_lines.shape

    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            curr_tree = input_lines[row, col]
            left_score = get_score(input_lines[row, :col][::-1], curr_tree)
            right_score = get_score(input_lines[row, col + 1 :], curr_tree)
            up_score = get_score(input_lines[:row, col][::-1], curr_tree)
            down_score = get_score(input_lines[row + 1 :, col], curr_tree)
            tree_score[row, col] = left_score * right_score * up_score * down_score

    return np.max(tree_score)


if __name__ == "__main__":
    input_lines = read_input_lines()
    print(part_one(input_lines))
    print(part_two(input_lines))
