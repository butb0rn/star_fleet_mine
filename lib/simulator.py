import grid
import script
import vessel


class Simulator:
    def __init__(self):
        self.grid = grid.Grid()
        self.script = script.script()
        self.vessel = vessel.Vessel()
        self.commands = []
        self.step = 1
        self.mine_map = self.grid.get_grid_file()

    def run(self):
        self.commands = self.script.get_commands()
        #find active mines

        for command in self.commands:
            #put conditions to break the loop
            self.print_step()
            self.grid.print_grid(self.mine_map)
            #get command with the loop
            self.script.print_command(command)
            for order in command.split():
                self.mine_map = self.execute_command(order)
            self.grid.print_grid(self.mine_map)

        self.vessel.print_score()

    def execute_command(self, order):
        map_after_instruct = self.vessel.execute_command(order, self.mine_map)
        return map_after_instruct


    def print_step(self):
        print '{}{}'.format('Step ',self.step)
        self.step += 1
        print

