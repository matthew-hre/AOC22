def parse_input() -> list:
    f = open("input.txt", "r")
    data = f.read()
    f.close()

    # BASIC INTEGER PARSING

    return list(map(int, data.split()))


def main():
    data = parse_input()


main()
