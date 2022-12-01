def parse_input() -> list:
    f = open("day1/input.txt", "r")
    data = f.read()
    f.close()

    # BASIC INTEGER PARSING

    return [sum([int(x) for x in x.split("\n")]) for x in data.split("\n\n")]


def main():
    data = parse_input()
    total = 0

    for i in range(3):
        total += max(data)
        data.remove(max(data))

    print(total)


main()
