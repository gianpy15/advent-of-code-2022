from __future__ import annotations

import operator
from functools import reduce
from pathlib import Path
from typing import Callable

import numpy as np
from pydantic import BaseModel


class Monkey(BaseModel):
    index: int
    inspections: int = 0
    starting_items: list[int] = []
    items: list[int] = []
    operation: Callable = None
    left_operand: int | None = None
    right_operand: int | None = None
    divisibility_test: int = 0
    true: int = 0
    false: int = 0

    def inspect(self, monkeys: dict[str, Monkey]):
        self.starting_items += self.items
        self.items.clear()
        for item in self.starting_items:
            self.inspections += 1
            item = self.operation(self.left_operand or item, self.right_operand or item)
            item //= 3
            if item % self.divisibility_test == 0:
                monkeys[self.true].items.append(item)
            else:
                monkeys[self.false].items.append(item)
        self.starting_items.clear()

    def better_inspect(self, monkeys: dict[str, Monkey]):
        self.starting_items += self.items
        self.items.clear()
        factor = reduce(
            operator.mul, [monkey.divisibility_test for monkey in monkeys.values()], 1
        )
        for item in self.starting_items:
            self.inspections += 1
            item = self.operation(self.left_operand or item, self.right_operand or item)
            if item % self.divisibility_test == 0:
                monkeys[self.true].items.append(item % factor)
            else:
                monkeys[self.false].items.append(item % factor)
        self.starting_items.clear()

    def __str__(self) -> str:
        return f"Monkey {self.index}: {self.inspections}, [{', '.join(str(item) for item in self.items)}]"


def read_input_lines(monkeys: dict[str, Monkey]) -> dict[str, Monkey]:
    file_path = Path(__file__).parent / "input.txt"
    current_monkey = 0
    for line in file_path.read_text().splitlines():
        line = line.replace(":", "")
        match line.split():
            case ["Monkey", index]:
                current_monkey = Monkey(index=int(index))
                monkeys[int(index)] = current_monkey
            case ["Starting", "items", *items]:
                current_monkey.starting_items = [int(x.replace(",", "")) for x in items]
            case ["Operation", "new", "=", left, operand, right]:
                try:
                    current_monkey.left_operand = int(left)
                except ValueError:
                    current_monkey.left_operand = None
                try:
                    current_monkey.right_operand = int(right)
                except ValueError:
                    current_monkey.right_operand = None
                current_monkey.operation = (
                    operator.add if operand == "+" else operator.mul
                )
            case ["Test", "divisible", "by", value]:
                current_monkey.divisibility_test = int(value)
            case ["If", "true", "throw", "to", "monkey", index]:
                current_monkey.true = int(index)
            case ["If", "false", "throw", "to", "monkey", index]:
                current_monkey.false = int(index)

    return monkeys


def part_one(monkeys: dict[str, Monkey]) -> int:
    for _ in range(20):
        for monkey in monkeys.values():
            monkey.inspect(monkeys)

    sorted_monkeys = sorted(
        list(monkeys.values()), key=lambda monkey: monkey.inspections, reverse=True
    )
    return sorted_monkeys[0].inspections * sorted_monkeys[1].inspections


def part_two(monkeys: dict[str, Monkey]) -> int:
    for _ in range(10000):
        for monkey in monkeys.values():
            monkey.better_inspect(monkeys)

    sorted_monkeys = sorted(
        list(monkeys.values()), key=lambda monkey: monkey.inspections, reverse=True
    )
    return sorted_monkeys[0].inspections * sorted_monkeys[1].inspections


if __name__ == "__main__":
    monkeys: dict[str, Monkey] = {}
    monkeys = read_input_lines(monkeys)
    print(part_one(monkeys))
    monkeys = read_input_lines(monkeys)
    print(part_two(monkeys))
