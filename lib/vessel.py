import grid

class Vessel:
    def __init__(self):
        self.commands = ["alpha", "beta", "gamma", "delta", "north", "south", "east", "west"]

    def execute_command(self, command, mine_map):

        new_map = grid.Grid.adjust_grid(mine_map)
        return new_map


    def print_score(self):
        print "Final score"
