# Constants for counter bounds and initial value
COUNTER_MIN = 0
COUNTER_MAX = 99
COUNTER_START = 50


class SafeCombinationDecoder:
    """
    Decodes a safe combination by processing movement instructions.

    The decoder maintains a counter that wraps around in a circular buffer
    (0-99), processing left (L) and right (R) movement instructions,
    and counts how many times the counter lands on 0.
    """

    def __init__(self, instructions: list[str]):
        """
        Initialize the decoder with a list of instructions.
        """
        self.instructions = instructions

    @classmethod
    def from_file(cls, filepath: str) -> "SafeCombinationDecoder":
        """
        Create a SafeCombinationDecoder from a file.
        """
        with open(filepath, "r") as file:
            instructions = file.read().strip().splitlines()
        return cls(instructions)

    def _move_left(self, counter: int, amount: int) -> int:
        """
        Move the counter left (decrease) with wrapping.
        """
        return (counter - amount) % 100

    def _move_right(self, counter: int, amount: int) -> int:
        """
        Move the counter right (increase) with wrapping.
        """
        return (counter + amount) % 100

    def decode(self) -> int:
        """
        Process all instructions and count how many times counter reaches 0.
        """
        counter = COUNTER_START
        answer = 0

        for instruction in self.instructions:
            direction = instruction[0]
            amount = int(instruction[1:])

            # Normalize amounts greater than 100
            if amount > 100:
                amount = amount % 100

            if direction == "L":
                counter = self._move_left(counter, amount)
            else:  # direction == "R"
                counter = self._move_right(counter, amount)

            if counter == 0:
                answer += 1

        return answer


def main():
    safe_decoder = SafeCombinationDecoder.from_file("input.txt")
    answer = safe_decoder.decode()
    print(f"The final answer is: {answer}")


if __name__ == "__main__":
    main()
