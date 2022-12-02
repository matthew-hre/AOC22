from template import Template


class Day2(Template):
    def __init__(self):
        self.day = 2
        super().__init__(self.day)

        self.set_data([x.split(" ") for x in self.get_data().split("\n")])

        self.dict = {
            "X": 1,
            "Y": 2,
            "Z": 3,
            "A": 1,
            "B": 2,
            "C": 3,
        }

    def part1(self):
        data = self.get_data()

        dict = self.dict

        wins = ["CX", "AY", "BZ"]
        losses = ["AZ", "BX", "CY"]

        score = 0

        for item in data:
            if dict[item[0]] == dict[item[1]]:
                score += 3 + dict[item[1]]
                continue

            score += 6 + dict[item[1]] if item[0] + \
                item[1] in wins else dict[item[1]]

        return score

    def part2(self):
        data = self.get_data()
        dict = self.dict
        score = 0

        losses = {
            "A": "Z",
            "B": "X",
            "C": "Y"
        }

        wins = {
            "A": "Y",
            "B": "Z",
            "C": "X"
        }

        for item in data:
            if dict[item[1]] == 1:  # lose
                score += dict[losses[item[0]]]

            if dict[item[1]] == 2:  # draw
                score += 3 + dict[item[0]]

            if dict[item[1]] == 3:  # win
                score += 6 + dict[wins[item[0]]]

        return score


print(Day2())
