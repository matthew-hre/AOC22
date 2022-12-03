from template import Template


class Day_01(Template):
    def __init__(self):
        self.day = 1
        super().__init__(self.day)

        self.set_data([sum([int(x) for x in x.split("\n")])
                      for x in self.get_data().split("\n\n")])

    def part1(self):
        return max(self.get_data())

    def part2(self):
        data = self.get_data()
        total = 0

        for i in range(3):
            total += max(data)
            data.remove(max(data))

        return total


print(Day_01())
