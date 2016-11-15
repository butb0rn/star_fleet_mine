import grid

class Vessel:
    def __init__(self):
        self.commands = {0: self.alpha, 1: self.beta, 2: self.gamma, 3: self.delta,
                         4: self.north, 5: self.south, 6: self.east, 7: self.west, 8: self.wrong_command}
        self.x = 0
        self.y = 0
        self.z = 0
        self.shots_fired = 0
        self.grid = None
        self.moves = 0



    def execute_command(self, command, mine_map, grid):
        num_command = self.map_command(command)
        self.grid = grid
        self.commands[num_command]()
        new_map = grid.adjust_grid(mine_map)
        return new_map

    def map_command(self, command):
        if command == "alpha":
            return 0
        elif command == "beta":
            return 1
        elif command == "gamma":
            return 2
        elif command == "delta":
            return 3
        elif command == "north":
            return 4
        elif command == "south":
            return 5
        elif command == "east":
            return 6
        elif command == "west":
            return 7
        else:
            return 8


    def print_score(self):
        print "Final score"

    def find_mines_on_map(self, x, y, z):
        mines = []
        for i in range(0, len(self.grid.active_mines_x)):
            if (self.grid.active_mines_x[i] == x) and (self.grid.active_mines_y[i] == y):
                mines.append(i)

        return mines

    def destroy_mine(self, i):
        self.grid.inactive_mines_x.append(self.grid.active_mines_x[i])
        self.grid.inactive_mines_y.append(self.grid.active_mines_y[i])
        self.grid.inactive_mines_z.append(self.grid.active_mines_z[i])
        self.grid.active_mines_x.pop(i)
        self.grid.active_mines_y.pop(i)
        self.grid.active_mines_z.pop(i)

    def alpha(self):
        print "alpha is here"
        mines_se = self.find_mines_on_map(self.x + 1, self.y+1, self.z)
        for mine in mines_se:
            self.destroy_mine(mine)

        mines_sw = self.find_mines_on_map(self.x - 1, self.y+1, self.z)
        for mine in mines_sw:
            self.destroy_mine(mine)

        mines_ne = self.find_mines_on_map(self.x + 1, self.y-1, self.z)
        for mine in mines_ne:
            self.destroy_mine(mine)

        mines_nw = self.find_mines_on_map(self.x - 1, self.y-1, self.z)
        for mine in mines_nw:
            self.destroy_mine(mine)

        self.shots_fired += 1




    def beta(self):
        print "beta is here"
        mines_n = self.find_mines_on_map(self.x, self.y-1, self.z)
        for mine in mines_n:
            self.destroy_mine(mine)

        mines_s = self.find_mines_on_map(self.x, self.y+1, self.z)
        for mine in mines_s:
            self.destroy_mine(mine)

        mines_e = self.find_mines_on_map(self.x + 1, self.y, self.z)
        for mine in mines_e:
            self.destroy_mine(mine)

        mines_w = self.find_mines_on_map(self.x - 1, self.y, self.z)
        for mine in mines_w:
            self.destroy_mine(mine)

        self.shots_fired += 1

    def gamma(self):
        print "gamma is here"
        mines_e = self.find_mines_on_map(self.x + 1, self.y, self.z)
        for mine in mines_e:
            self.destroy_mine(mine)

        mines_w = self.find_mines_on_map(self.x - 1, self.y, self.z)
        for mine in mines_w:
            self.destroy_mine(mine)

        mines = self.find_mines_on_map(self.x, self.y, self.z)
        for mine in mines:
            self.destroy_mine(mine)

        self.shots_fired += 1

    def delta(self):
        print "delta is here"
        mines_n = self.find_mines_on_map(self.x, self.y-1, self.z)
        for mine in mines_n:
            self.destroy_mine(mine)

        mines_s = self.find_mines_on_map(self.x, self.y+1, self.z)
        for mine in mines_s:
            self.destroy_mine(mine)

        mines = self.find_mines_on_map(self.x, self.y, self.z)
        for mine in mines:
            self.destroy_mine(mine)

    def north(self):
        print "north is here"
        self.y -= 1
        self.moves += 1

    def south(self):
        print "south is here"
        self.y += 1
        self.moves += 1

    def east(self):
        print "east is here"
        self.x += 1
        self.moves += 1

    def west(self):
        print "west is here"
        self.x -= 1
        self.moves += 1

    def wrong_command(self):
        print "Wrong command input"

