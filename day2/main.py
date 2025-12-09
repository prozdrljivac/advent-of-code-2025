import re


def find_invalid_ids(start, end):
    invalid_ids = set()
    for id in range(start, end + 1):
        test_id = str(id)
        invalid_id = re.search(r"^(\d+)\1+$", test_id)
        # NOTE: Part one solution
        # if invalid_id and test_id.count(invalid_id.group(1)) == 2:
        #     invalid_ids.add(id)
        # NOTE: Part two solution
        if invalid_id and test_id.count(invalid_id.group(1)) >= 2:
            invalid_ids.add(id)

    return invalid_ids


def main():
    invalid_ids = []
    with open("input.txt", "r") as input_file:
        ranges = input_file.read().split(",")
    for rng in ranges:
        start, end = map(int, rng.split("-"))
        invalid_ids.extend(find_invalid_ids(start, end))
    invalid_ids = set(invalid_ids)
    result = sum(invalid_ids)
    print(result)


if __name__ == "__main__":
    main()
