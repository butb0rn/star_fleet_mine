class Grid:
    def __init__(self):
        pass

    def get_grid_file(self):
        with open("field.txt") as textFile:
            grid = [[digit for digit in line.strip()] for line in textFile]
        return grid

    def print_grid(self, grid):
        for i in range(len(grid)):
            print("".join(grid[i]))
        print

    @staticmethod
    def adjust_grid(grid):
        grid = [[".","a","."],[".",".","a"]]
        return grid


