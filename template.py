import requests
from functools import cache
from typing import Any

session = requests.Session()

# i just downloaded this manually lol
cookie_file = open("cookie.txt", "r")
cookie = cookie_file.read().strip()
cookie_file.close()

# ensures the site gives us the correct data, and not just a lame "you're not logged in" reponse
requests.utils.add_dict_to_cookiejar(session.cookies, {"session": cookie})


@cache
def get_input_data(day: int) -> str:
    """Takes a day and returns the input data for that day

    Args:
        day (int): The day to get the input data for

    Returns:
        str: The unparsed input data
    """
    url = f"https://adventofcode.com/2022/day/{day}/input"
    return session.get(url).text.strip()


class Template:
    def __init__(self, day: int):
        """Initializes the template class"""
        self.day = day
        self.link = f"https://adventofcode.com/2022/day/{day}"
        self.__data = get_input_data(day)

    def get_data(self) -> Any:
        """Gets the data for the day
        WARNING: The data may be any type, as it can be modified by the set_data method

        Returns:
            Any: The data for the day
        """
        return self.__data

    def set_data(self, data: Any) -> None:
        """Sets the data as the given data
        WARNING: The data may be any type

        Args:
            data (Any): The data to set the data to
        """
        self.__data = data

    def part1(self) -> int:
        """Returns the numerical answer for part 1"""
        pass

    def part2(self) -> int:
        """Returns the numerical answer for part 2"""
        pass

    def __str__(self) -> str:
        """Returns the string representation of the day"""
        newline = "\n"
        return f"{newline * 50}--- ADVENT OF CODE DAY {self.day} ---\n{self.link}\n\nPart One: {self.part1()}\nPart Two: {self.part2()}"
