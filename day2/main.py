import re


def find_invalid_ids(start, end):
    pattern = re.compile(r"^(\d+)\1+$")
    invalid_ids = []
    for id in range(start, end + 1):
        test_id = str(id)
        invalid_id = pattern.match(test_id)
        # NOTE: Part one solution
        # if invalid_id and test_id.count(invalid_id.group(1)) == 2:
        #     invalid_ids.add(id)
        # NOTE: Part two solution
        if invalid_id and test_id.count(invalid_id.group(1)) >= 2:
            invalid_ids.append(id)

    return invalid_ids


def main():
    invalid_ids = set()
    with open("input.txt", "r") as input_file:
        ranges = input_file.read().split(",")
    for rng in ranges:
        start, end = map(int, rng.split("-"))
        invalid_ids.update(find_invalid_ids(start, end))
    result = sum(invalid_ids)
    print(result)


if __name__ == "__main__":
    main()
