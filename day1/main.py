from typing import Self

class SafeCombinationDecoder:
    def __init__(self: Self, input_file_path: str):
        with open(input_file_path, "r") as safe_combination_file:
            safe_combination_file.seek(0)
            self.safe_combination = safe_combination_file.read().strip().splitlines()


def main():
    safe_decoder = SafeCombinationDecoder("input.txt")
    print(safe_decoder.safe_combination)


if __name__ == "__main__":
    main()
