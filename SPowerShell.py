import os
from datetime import datetime
from re import fullmatch
print("-"*100)
print("Sparrow PowerShell")
print("Copyright (C) Sparrow Corporation. All rights reserved\n") # Dont take this seriously 🙏
print(f"Welcome to Sparrow Powershell\n")
print("\nType 'help' for a list of commands")

def cmd_help():
    print("""
Sparrow PowerShell - List of Available commands :
          
1. echo <text>               -> outputs x
2. cls                       -> Clears the terminal
3. del <file path>           -> removes/deletes a file
4. New-Item <name>           -> creates a file named <name>.txt
5. time                      -> Shows current time
6. ls                        -> Lists the items in the subdirectory
7. pwd                       -> outputs the present directory the user is in
8. gc                        -> Opens the content of files in pwd
9. cd <path>                 -> Changes the current directory to <path>
10. calc <expr>              -> calculates an expression
11. edit <file editor>       -> Edits the file
12. exit                     -> exits the Sparrow PowerShell
""")

def cmd_echo(x):  # This is echo
    print(x)

def cmd_cls():
    os.system('cls' if os.name == 'nt' else 'clear') # This is the cls segment

def cmd_del(file_path):                         
    try:
        if file_path == r"C:\Windows\System32":
            print("Cannot remove Critical system files")
        elif os.path.exists(file_path):
            os.remove(file_path)                            # Well, This is the file deletion segment
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

def cmd_calc(x):
    def mathexpr(s):
        return bool(fullmatch(r"[0-9+\-*/().\s]+",s))
    if mathexpr(x) == True:
        print(eval(x))
    else:
        print("Enter a valid expression")

def cmd_edit(x):
    os.system(x)


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
    "gc" : cmd_gc,
    "calc" : cmd_calc,
    "edit" : cmd_edit
}

while True:                                                 #Looks cluttered and is cluttered
    try:                                                    # For the changing directories in the PowerShell prompt
        cwd = os.getcwd()    
        Input = input(f"S-PS {cwd}> ").split()
        
        if Input[0] in commands:                            # The first token of input checking 
            if len(Input) > 1:
                commands[Input[0]](" ".join(Input[1:]))     #If input > 1, it adds the Input[1] token in parentheses beside the Input[0], Basically a function call
            else:                                           #input[1:] is slicing, Excludes input[0] and joins the rest to the initial function call
                commands[Input[0]]()                        # If it's not >1, it just becomes the function call.
        elif Input[0] == "exit":
            break
        else:
            print(f"No such command as {Input} Exists.")    # Error exception
    except Exception as e:

        print(f"Error: \n{e}")
