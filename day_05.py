from template import Template
import copy


class Day_05(Template):
    def __init__(self):
        self.day = 5
        super().__init__(self.day)

        self.crane = self.get_crane()

        self.set_data([list(map(int, x.split(' ')[1::2]))
                       for x in self.get_data().strip().split("\n\n")[1].split("\n")])

    def part1(self):
        data = self.get_data()
        crane = copy.deepcopy(self.crane)

        for item in data:
            print(item)
            count = item[0]
            start = item[1] - 1
            end = item[2] - 1
            for c in range(count):
                grabbed = crane[start].pop()
                crane[end].append(grabbed)

        return "".join([x[-1] for x in crane])

    def part2(self):
        data = self.get_data()
        crane = copy.deepcopy(self.crane)

        for item in data:
            count = item[0]
            start = item[1] - 1
            end = item[2] - 1

            items = []
            for c in range(count):
                grabbed = crane[start].pop()
                items.append(grabbed)

            crane[end] += items[::-1]

        return "".join([x[-1] for x in crane])

    def get_crane(self):
        # hatred and malice
        crane = self.get_data().split("\n\n")[0].split("\n")
        crane = [[line[i:i+4]
                 for i in range(0, len(line), 4)] for line in crane]
        crane = list(zip(*crane))
        crane = [list(reversed(list(x)[:-1])) for x in crane]
        crane = [list(filter(lambda x: x != '    ', line))
                 for line in crane]
        crane = [list(filter(lambda x: x != "", [y.replace(' ', '').replace(
            '[', '').replace(']', '') for y in x])) for x in crane]

        return crane


print(Day_05())
