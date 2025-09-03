import os
from datetime import datetime
print("Sparrow PowerShell")
print("Copyright (C) Sparrow Corporation. All rights reserved\n") # Dont take this seriously 🙏
print("Welcome to Sparrow Powershell\n\n")

# Please help me improve this cmd_help
def cmd_help():
    print("""List of Available commands :\n1. echo(x) -> outputs x\n2. cls -> Clears the terminal\n3. del x -> removes/deletes a file\n4. New-Item -> creates a file\n5. time -> Shows current time\n6. ls -> Lists the items in the subdirectory\n7. pwd -> outputs the present directory the user is in\n7. gc -> Opens the content of files in pwd""")

def cmd_echo(x):  # This is echo
    print(x)

def cmd_cls():
    os.system('cls' if os.name == 'nt' else 'clear') # This is the cls segment

def cmd_del(file_path):                         
    try:
        if file_path == r"C:\Windows\System32":
            print("Cannot remove Critical system files")
        elif os.path.exists(file_path):
            os.remove(file_path)                                               # Well, This is the file deletion segment
        else:
            print(f"File '{file_path}' not found.")
    except PermissionError:
        print("File removal denied. Insufficient Permission level")
    except Exception as e:
        print(f"An unexpected error occurred:\n\n{e}")

def cmd_newitem(filename):   #The file creation segment
    open(filename+".txt", "w").close()

def cmd_time():     #The datetime segment
    print(datetime.now())

def cmd_ls():       #ls, lists subdirectories
    a = os.listdir()
    for char in a:
        print(char)

def cmd_pwd():      # pwd, prints the current directory
    print(os.getcwd())

def cmd_cd(path):   # cd, change directory
    os.chdir(path)

def cmd_gc(filename): #gc, Get-Contents
    try:
        with open(filename, "r", errors="ignore") as f:
            print(f.read())
    except Exception as e:
        print(f"An error occurred:\n{e}")
    
    
# List of commands
commands = {
    "help" : cmd_help,
    "echo" : cmd_echo,
    "cls" : cmd_cls,
    "del" : cmd_del,
    "New-Item" : cmd_newitem,
    "time" : cmd_time,
    "ls" : cmd_ls,
    "pwd" : cmd_pwd,
    "cd" : cmd_cd,
    "gc" : cmd_gc
}


while True:                                             #Looks cluttered and is cluttered
    try:                                         # For the changing directories in the PowerShell prompt
        cwd = os.getcwd()    
        Input = input(f"S-PS {cwd}> ").split()  # Input
        if Input[0] in commands:                # The first token of input checking 
            if len(Input) > 1:
                commands[Input[0]](" ".join(Input[1:])) #If input > 1, it adds the Input[1] token in brackets beside the Input[0], Basically a function call
            else:
                commands[Input[0]]()            # If it's not >1, it just becomes the function call.
        elif Input[0] == "exit":
            break
        else:
            print(f"No such command as {Input} Exists.")        # Error exception
    except Exception as e:

        print(f"Error: \n{e}")



