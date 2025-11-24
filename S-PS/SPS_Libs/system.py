import os
from datetime import datetime

def cmd_cls():
    os.system('cls' if os.name == 'nt' else 'clear') # This is the cls segment

def cmd_time():     #The datetime segment
    print(datetime.now())

def cmd_pwd():      # pwd, prints the current directory
    print(os.getcwd())

def cmd_cd(path):   # cd, change directory
    os.chdir(path)

def cmd_help():
    print("""
------------------------------------------------------------------------------------------------------------------------   
                                            Sparrow PowerShell - Help :

• For help about a certain command, type <command name> --help
    example :
          ping --help

• For a list of all commands, open COMMANDS.md in GitHub.
Thank you for using S-PS
------------------------------------------------------------------------------------------------------------------------
"""
)