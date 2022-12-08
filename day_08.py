from template import Template


class Day_08(Template):
    def __init__(self):
        self.day = 8
        super().__init__(self.day)

        self.set_data([list(map(int, list(x)))
                      for x in self.get_data().strip().split("\n")])

    def part1(self):
        data = self.get_data()
        visible = 0

        for row_idx in range(len(data)):
            for col_idx in range(len(data[row_idx])):
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                can_add = False

                for dir in dirs:
                    if self.is_visible(row_idx, col_idx, dir[0], dir[1], data[row_idx][col_idx]):
                        can_add = True

                visible += 1 if can_add else 0

        return visible

    def part2(self):
        data = self.get_data()

        scenic_score = 0

        for row_idx in range(len(data)):
            for col_idx in range(len(data[row_idx])):

                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                new_score = 1

                for dir in dirs:
                    new_score *= self.get_scenic(row_idx, col_idx,
                                                 dir[0], dir[1], data[row_idx][col_idx])

                scenic_score = new_score if new_score > scenic_score else scenic_score

        return scenic_score

    def is_visible(self, x, y, xx, yy, height):
        if (x+xx < 0) or (y+yy < 0) or (y+yy > len(self.get_data()) - 1) or (x+xx > len(self.get_data()[0]) - 1):
            return True

        if self.get_data()[x + xx][y + yy] >= height:
            return False

        return self.is_visible(x+xx, y+yy, xx, yy, height)

    def get_scenic(self, x, y, xx, yy, height, count=0):
        if (x+xx < 0) or (y+yy < 0) or (y+yy > len(self.get_data()) - 1) or (x+xx > len(self.get_data()[0]) - 1):
            return count

        if self.get_data()[x + xx][y + yy] >= height:
            return count + 1

        return self.get_scenic(x+xx, y+yy, xx, yy, height, count+1)


print(Day_08())
