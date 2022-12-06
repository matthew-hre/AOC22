from template import Template


class Day_06(Template):
    def __init__(self):
        self.day = 6
        super().__init__(self.day)

        self.set_data(list(self.get_data()))

    def part1(self):
        return self.get_unique_position(4)

    def part2(self):
        return self.get_unique_position(14)

    def get_unique_position(self, char_count: int) -> int:
        data = self.get_data()
        current_chars = []

        for count in range(len(data)):
            current_chars.append(data[count])

            if len(current_chars) > char_count:
                current_chars.remove(current_chars[0])

            if len(set(current_chars)) == char_count:
                return count + 1


print(Day_06())
