import re


def find_invalid_ids(start, end):
    invalid_ids = set()
    for id in range(start, end + 1):
        test_id = str(id)
        invalid_id = re.search(r"^(\d+?)\1+$", test_id)
        if invalid_id:
            invalid_ids.add(int(invalid_id.group(1)))

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


# TODO - I am getting a number that is too high, check what the issue is
if __name__ == "__main__":
    main()
