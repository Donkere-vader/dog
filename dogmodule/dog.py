import os
import json


class Dog:
    def __init__(self, file="dog.json", folder="dog"):
        files = os.listdir()

        self.file, self.folder = file, folder

        # check if dog is instanciated
        if self.file in files:
            file_loc = self.file
        elif self.folder in files and os.path.isdir(self.folder) and self.file in os.listdir(self.folder):
            file_loc = f"{self.folder}/{self.file}"
        else:
            print(f"No {self.file} or {self.folder}/{self.file} file found.")
            exit()

        self.commands = self.load_commands(file_loc)['commands']

    def load_commands(self, json_file):
        return json.load(open(json_file, 'r'))

    def command(self, command):
        try:
            command = self.commands[command]
        except KeyError:
            raise Exception(f"No command '{command}' found in {self.file} or {self.folder}/{self.file}")

        if type(command) == dict:
            command = f"{self.folder}/{command['file']}"

        os.system(command)
