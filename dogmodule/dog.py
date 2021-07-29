import os
import yaml



class Dog:
    def __init__(self, command, file):
        self.file = file

        if self.file not in os.listdir() + os.listdir(os.environ['HOME']):
            print(f"Couldn't find '{self.file}' in current working directory or '{os.environ['HOME']}'")
            exit(1)

        self.info: dict = {}
        with open(self.file, 'r') as f:
            self.info: dict = yaml.load(f, Loader=yaml.FullLoader)
        
        if 'commands' not in self.info:
            print(f"Please supply commands in the '{self.file}' dog file")
            exit(1)

        self.run_command(command)

    def run_command(self, command):
        print(f"Running DOG command: {command}")

        if command not in self.info['commands']:
            print(f"Command '{command}' not found in dog file: '{self.file}'")
            exit(1)

        code = [line.strip() for line in str(self.info['commands'][command]['code']).split(";")]

        while "" in code:
            code.remove("")

        for line in code:
            print()
            print("$ " + line.replace('\n', '\\n'))
            os.system(line)
