import re
class Grid:
    def __init__(self):
        self.active_mines_x = []
        self.active_mines_y = []
        self.active_mines_z = []
        self.inactive_mines_x = []
        self.inactive_mines_y = []
        self.inactive_mines_z = []
        self.grid_field = self.get_grid_file()
        self.number_mines = 0



    def get_grid_file(self):
        with open("field.txt") as textFile:
            grid = [[digit for digit in line.strip()] for line in textFile]

        return grid

    def add_mine(self, x, y, z):
        self.active_mines_x.append(x)
        self.active_mines_y.append(y)
        self.active_mines_z.append(z)

    def find_active_mines(self):
        for i in range(len(self.grid_field)):
            for j in range(len(self.grid_field[0])):
                if self.grid_field[i][j] == '.':
                    pass
                elif re.match('[a-zA-Z]', self.grid_field[i][j]):
                    self.add_mine(i, j, ord(self.grid_field[i][j]))
                    self.number_mines += 1



    def print_grid(self, grid):
        for i in range(len(grid)):
            print("".join(grid[i]))
        print


    def adjust_grid(self, grid):
        # grid = [[".","a","."],[".",".","a"]]
        return grid



