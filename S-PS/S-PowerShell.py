import os, sys
from SPS_loader import load_metadata, load_commands
from SPS_Libs.system import cmd_cls
cmd_cls()
print(f"{'\t'*6}Sparrow PowerShell\n{'-'*140}\n\n")                                               # By treating them as separate lines
print("Copyright (C) Sparrow Corporation. All rights reserved (Does not exist)\n") # Dont take this seriously 🙏
print("Welcome to Sparrow Powershell\n")
print("\nType 'help' for a list of commands and '/exit' to exit S-PS")

metadata = load_metadata()
commands = load_commands()

def parse_file_io(x, op, cmd_name):
    global commands
    mode = "a" if op == ">>" else "w"
    op_index = x.index(op)
    before, after = x[:op_index], " ".join(x[op_index +1:])
    cmd_output = commands[cmd_name](" ".join(before[1:])) if len(before) > 1 else commands[" ".join(before)]()
    with open(after, mode) as f:
        f.write(f"{cmd_output}\n")


def _execute_command(tokens):
    global metadata, commands
    cmd_name = tokens[0]
    if cmd_name == "/exit":
        sys.exit()
    if ">" in tokens or ">>" in tokens:
        op = ">" if ">" in tokens else ">>"
        parse_file_io(tokens, op, cmd_name)
    elif len(tokens) > 1:
        if tokens[1] == "--help":
            if cmd_name in metadata:
                print(metadata[cmd_name])
            else:
                print("Metadata not found / Unable to fetch.")
        else:
            print(commands[cmd_name](" ".join(tokens[1:])))
    elif len(tokens) == 1:
        print(commands[cmd_name]())

while True:                                                 
    try:                                                    
        cwd = os.getcwd()                                   # Checks for && seperator and splits UserInput
        UserInput = input(f"\nS-PS {cwd}> ")                # The split list is then iterated and functions are called
        Input = UserInput.split()
        if "&&" in UserInput:
            no_of_commands = UserInput.split('&&')              
            for cmd in no_of_commands:                             # Here, tokens are the individual split commands
                tokens = cmd.strip().split()                       # Which are then called (tokens, as in individual characters like keywords etc)
                _execute_command(tokens) 

        elif "&&" not in UserInput:
            _execute_command(Input)
    #except Exception as e:
    #    print(f"Error: \n{e}")
    except KeyboardInterrupt:
        print("Type '/exit' to exit")