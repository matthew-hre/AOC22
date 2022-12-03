from template import Template


class Day3(Template):
    def __init__(self):
        self.day = 3
        super().__init__(self.day)

        self.letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.set_data(self.get_data().split())

    def part1(self):
        data = self.get_data()
        score = 0

        for line in data:
            first_half = line[:len(line)//2]
            second_half = line[len(line)//2:]

            for char in first_half:
                if char in second_half:
                    score += self.letters.index(char) + 1
                    break

        return score

    def part2(self):
        data = self.get_data()
        score = 0

        # check every 4th line
        for line_idx in range(0, len(data), 3):
            line = data[line_idx]
            line_two = data[line_idx + 1]
            line_three = data[line_idx + 2]

            for char in line:
                if char in line_two and char in line_three:
                    score += self.letters.index(char) + 1
                    break

        return score


print(Day3())
