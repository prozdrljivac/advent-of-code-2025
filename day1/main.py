from typing import Self

class SafeCombinationDecoder:
    def __init__(self: Self, input_file_path: str):
        self.limit_min = 0
        self.limit_max = 99
        self.counter = 50
        self.answer = 0
        with open(input_file_path, "r") as safe_combination_file:
            safe_combination_file.seek(0)
            self.safe_combination = safe_combination_file.read().strip().splitlines()

    def decode(self: Self) -> int:
        for number in self.safe_combination:
            sign = number[0]
            value = int(number[1:])

            if sign == "L":
                if self.counter - value == 0:
                    self.answer += 1
                elif self.counter - value < self.limit_min:
                   self.counter = self.limit_max - (value - self.counter) 
                else:
                    self.counter -= value
            else:
                if self.counter + value == 0:
                    self.answer += 1
                elif self.counter + value > self.limit_max:
                    self.counter = self.limit_min + ((value + self.counter) - self.limit_max)
                else:
                    self.counter += value
def main():
    safe_decoder = SafeCombinationDecoder("testinput.txt")
    safe_decoder.decode()
    print(f"The final answer is: {safe_decoder.answer}")


if __name__ == "__main__":
    main()
