import os
import yaml



class Dog:
    def __init__(self, command, list, file, verbose):
        self.file = file
        self.verbose = verbose
        self.list = list

        if self.file not in os.listdir():
            print(f"Couldn't find '{self.file}' in current working directory")
            exit(1)

        self.info: dict = {}
        with open(self.file, 'r') as f:
            self.info: dict = yaml.load(f, Loader=yaml.FullLoader)

        if 'commands' not in self.info:
            print(f"Please supply commands in the '{self.file}' dog file")
            exit(1)

        if self.list:
            self.show_list()
            exit(0)

        self.run_command(command)
    
    def show_list(self):
        print("List of available commands:\n")
        for cmd in self.info['commands']:
            print(f"  {cmd}")
            if 'description' in self.info['commands'][cmd]:
                print(f"    {self.info['commands'][cmd]['description']}")
        
        print()
        print("usage: ``dog COMMAND``")

    def run_command(self, command):
        if self.verbose: print(f"Running DOG command: {command}")

        if command not in self.info['commands']:
            print(f"Command '{command}' not found in dog file: '{self.file}'")
            print("For a list of commands run ``dog --list`` ")
            exit(1)

        code = [line.strip() for line in str(self.info['commands'][command]['code']).split(";")]

        while "" in code:
            code.remove("")

        for line in code:
            if self.verbose:
                print()
                print("$ " + line.replace('\n', '\\n'))
            os.system(line)
