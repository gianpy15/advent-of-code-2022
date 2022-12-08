from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class File(BaseModel):
    name: str
    size: int = 0
    files: list[File] | None = None
    parent: File | None = None

    @property
    def is_file(self):
        return self.files is None

    def add_file(self, file: File):
        self.files.append(file)
        file.parent = self

    def cd(self, file_name: str) -> File:
        for file in self.files:
            if file.name == file_name:
                return file

    def update_size(self) -> int:
        if self.is_file:
            return self.size

        self.size = sum(file.update_size() for file in self.files)
        return self.size

    def get_size_at_most(self, k: int) -> int:
        if self.is_file:
            return 0

        total_size = self.size if self.size <= k else 0
        for file in self.files:
            if file.is_file:
                continue
            total_size += file.get_size_at_most(k)

        return total_size

    def find_files_grather_than(self, k: int) -> list[int]:
        if self.is_file:
            return []

        sizes = [file.find_files_grather_than(k) for file in self.files]
        sizes = [item for sublist in sizes for item in sublist if item >= k]
        sizes.append(self.size)

        return sizes


def read_input_lines() -> File:
    file_path = Path(__file__).parent / "input.txt"
    commands = file_path.read_text().splitlines()
    root = File(name="/", files=[])
    current_dir = root
    for command in commands[1:]:
        match command.split():
            case ["dir", dir_name]:
                current_dir.add_file(File(name=dir_name, files=[]))
            case ["$", "ls"]:
                pass
            case [size, file_name]:
                current_dir.add_file(File(name=file_name, size=int(size)))
            case ["$", "cd", ".."]:
                current_dir = current_dir.parent
            case ["$", "cd", dir_name]:
                current_dir = current_dir.cd(file_name=dir_name)
            case _:
                pass
    root.update_size()
    return root


def part_one(root: File) -> int:
    return root.get_size_at_most(100000)


def part_two(root: File) -> int:
    total_space = 70000000
    space_needed = 30000000
    free_space = total_space - root.size
    return min(root.find_files_grather_than(space_needed - free_space))


if __name__ == "__main__":
    root = read_input_lines()
    print(part_one(root))
    print(part_two(root))
