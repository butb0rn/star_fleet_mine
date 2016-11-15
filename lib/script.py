class script:
    def __init__(self):
        pass

    def get_script_file(self):
        input_script = open("script.txt")
        return input_script

    def get_commands(self):
        return self.get_script_file()

    def print_command(self, command):
        print command