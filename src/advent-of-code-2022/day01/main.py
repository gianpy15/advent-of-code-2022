from pathlib import Path


def read_input_lines() -> list[str]:
    file_path = Path(__file__).parent / "input.txt"
    return file_path.read_text().splitlines()

def process_input(input_lines: list[str]) -> list[int]:
    input_lines = read_input_lines()
    inputs = [0]
    for input_ in input_lines:
        if input_ != "":
            inputs[-1] += int(input_)
        else:
            inputs.append(0)
    return inputs



if __name__ == "__main__":
    input_lines = read_input_lines()
    inputs = process_input(input_lines)
    
    print(max(inputs))
    print(sum(sorted(inputs, reverse=True)[:3]))

