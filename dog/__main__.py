#!/bin/python3

from dog import Dog
import sys


PROGRAM_FLAGS = {
    "h": "help",
    "f": "file"
}


def get_flag(arg):
    flag = None
    if arg.startswith("--"):
        flag = arg[2:]
    elif arg.startswith("-"):
        if arg[1:] in PROGRAM_FLAGS:
            flag = PROGRAM_FLAGS[arg[1:]]
        else:
            print(f"Unknown flag {arg}")
            exit()

    return flag


def get_command_argv() -> (tuple, dict):
    arguments = sys.argv
    del arguments[0]  # del program call

    args = []
    flags = {}

    head = 0
    while head < len(arguments):
        arg = arguments[head]

        flag = get_flag(arg)

        if flag is not None:
            if len(arguments) > head + 1 and not arguments[head + 1].startswith("-"):
                flags[flag] = arguments[head + 1]
                head += 2
            else:
                flags[flag] = ""
                head += 1
        else:
            args.append(arg)
            head += 1

    return args, flags


if __name__ == "__main__":

    args, flags = get_command_argv()

    try:
        command = args[0]
        del args[0]
    except IndexError:
        print("Please supply a command")
        exit()

    if "help" in flags:
        print("No help to display yet..")
        exit()

    dog = Dog(*args, **flags)
    dog.command(command)
