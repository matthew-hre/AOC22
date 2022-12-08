from template import Template


class Folder:
    def __init__(self, name: str, parent, size=None):
        self.name = name
        self.sub_folders = []
        self.parent = parent
        self.size = size if size else 0

    def add_folder(self, folder):
        self.sub_folders.append(folder)

    def set_size(self, size: int):
        self.size += size
        if self.parent:
            self.parent.set_size(size)

    def print_tree(self, level=0):
        print("  " * level + "/" + self.name +
              ": " + str(self.size) + " bytes")
        for sub in self.sub_folders:
            sub.print_tree(level + 1)

    def get_under_size(self):
        size = self.size if self.size <= 100000 else 0
        for sub in self.sub_folders:
            size += sub.get_under_size()
        return size

    def get_list_of_sizes(self, list_of_sizes=None):
        if list_of_sizes is None:
            list_of_sizes = []
        list_of_sizes.append(self.size)
        for sub in self.sub_folders:
            sub.get_list_of_sizes(list_of_sizes)
        return list_of_sizes

    def __str__(self):
        return f"{self.name} {self.size} {self.sub_folders}"


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} {self.size}"


class Day_07(Template):
    def __init__(self):
        self.day = 7
        super().__init__(self.day)

        self.location = Folder("/", None)
        self.root = self.location

        self.set_data(self.get_data().strip().split("\n"))

        self.get_file_system()

    def part1(self):
        self.root.print_tree()

        return self.root.get_under_size()

    def part2(self):
        maximum = 70_000_000
        needed = 30_000_000
        current = self.root.size + needed - maximum

        sizes = sorted(self.root.get_list_of_sizes())

        for idx in range(len(sizes)):
            current_size = sizes[idx]
            # 4473403
            if current_size - current > 0:
                return current_size

    def get_file_system(self):
        data = self.get_data()
        for line in data:
            line = line.split(" ")

            if line[0] == "$":
                if line[1] == "cd":
                    if line[2] == "..":
                        self.location = self.location.parent
                    else:
                        if line[2] == "/":
                            continue
                        new = Folder(line[2], self.location)
                        self.location.add_folder(new)
                        self.location = new
            elif line[0] != "dir":
                size = int(line[0])
                f = File(line[1], size)
                self.location.set_size(size)


print(Day_07())
