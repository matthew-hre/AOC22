from template import Template


class Day_04(Template):
    def __init__(self):
        self.day = 4
        super().__init__(self.day, "test.txt")

        self.set_data([[list(map(int, y.split("-"))) for y in x.split(",")]
                      for x in self.get_data().split()])

    def part1(self):
        count = 0
        for first, second in self.get_data():
            count += 1 if (first[0] <= second[0] and first[1] >= second[1]
                           ) or (second[0] <= first[0] and second[1] >= first[1]) else 0

        return count

    def part2(self):
        count = 0
        for first, second in self.get_data():
            count += 1 if bool(set(range(first[0], first[1] + 1))
                               & set(range(second[0], second[1] + 1))) else 0

        return count


print(Day_04())
