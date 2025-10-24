import os ; from datetime import datetime ; from re import fullmatch ; import json   # This ';' seperates the import lines
import subprocess ; import signal
print(f"{'-'*100}\nSparrow PowerShell")                                               # By treating them as separate lines
print("Copyright (C) Sparrow Corporation. All rights reserved (Does not exist)\n") # Dont take this seriously 🙏
print("Welcome to Sparrow Powershell\n")
print("\nType 'help' for a list of commands and 'exit' to exit S-PS")

def cmd_echo(x):  # This is echo
    if ">>" in x or ">" in x:
        if ">>" in x:
            op = ">>"
        elif ">" in x:
            op = ">"
        before, after = x.split(op, 1)
        message = before.rstrip()
        filename = after.strip()
        mode = "a" if op == ">>" else "w"
        with open(filename, mode) as f:
            f.write(message + "\n")
    else:
        print(x)

def cmd_pm_help():
    print("""            <----    Package manager Configuration Guide    ---->
          
    • When Running the 'install' or 'uninstall' command for the first time, an input prompt appears.
          
    • In the input prompt, Enter your system's package manager and its install command.
          
    • Do the same for uninstall command.
          
    -------------------------------------------------------------------------------------------------
                                    <----    Example    ---->
           
    • For winget, type 'winget install' for install cmd in the input prompt
          
    • For running the uninstall cmd, type 'winget uninstall' in the input prompt
          
    • Google the install and uninstall command if you don't remember. Thank you...
    -------------------------------------------------------------------------------------------------
                
    • To edit the saved (.json) file, enter > edit notepad config.json
          
    • When editing, avoid editing the Left Hand Side Keys for the json dict, that can cause the json to be created again
    """)
    
def cmd_cls():
    os.system('cls' if os.name == 'nt' else 'clear') # This is the cls segment

def cmd_del(file_path):
    if os.name == "nt":
        protected = [
            r"C:\Windows", r"C:\Program Files", r"C:\Program Files (x86)",
            r"C:\Users\Default", r"C:\Users\Public"
        ]
    elif os.name == "posix":
        protected = (
            "/bin", "/sbin", "/usr/bin", "/usr/sbin",
            "/lib","/lib64", "/etc", "/boot", "/root"
        )

    try:
        if any(os.path.abspath(file_path).startswith(p) for p in protected):
            print("Cannot remove Critical system files")
        elif os.path.exists(file_path):
            os.remove(file_path)                            # Well, This is the file deletion segment
            print
        else:
            print(f"File '{file_path}' not found.")
    except PermissionError:
        print("File removal denied. Insufficient Permission level")
    except Exception as e:
        print(f"An unexpected error occurred:\n\n{e}")

def cmd_newitem(filename):   #The file creation segment
    if os.name == "nt":
        open(f"{filename}", "w")
        print(f"\t\t Directory: {os.getcwd()}")
        print( "Mode           : -a----\n"
              f"LastWriteTime  : {datetime.now()} \n"
               "Length         : 0\n"
              f"name           : {filename}"
            )
    else:
        os.system(f"touch {filename}")
        print( "Mode           : Created (touch)\n"
              f"LastWriteTime  : {datetime.now()} \n"
               "Length         : 0\n"
              f"name           : {filename}"
            )
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
        with open(filename, "r") as f:
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

def cmd_pip(package_name):
    os.system(f"pip {package_name}")

def cmd_Install(package_name):
    config_file = "config.json"
    def load_config():
        if not os.path.exists(config_file):
            return {}
        try:
            with open (config_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    def save_config(config):
        with open(config_file, "w") as f:
            json.dump(config, f, indent=4 ) 
    config = load_config()
    if "package_manager" not in config or not config["package_manager"]:
        pm = input("Enter your package manager and its install command\n(apt, winget, yay, paru, choco etc): ")
        config["package_manager"] = pm.strip()
        save_config(config)

        print("Using package manager: ",
        config["package_manager"])
    os.system(f"{config['package_manager']} {package_name}")

def cmd_Uninstall(package_name):
    config_file = "config.json"
    def load_config():
        if not os.path.exists(config_file):
            return {}
        try:
            with open (config_file, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    def save_config(config):
        with open(config_file, "w") as f:
            json.dump(config, f, indent=4 ) 
    config = load_config()
    if "pm_uninstall" not in config or not config["pm_uninstall"]:
        pm = input("Enter your package manager and its uninstall command\n(apt, winget, yay, paru, choco etc): ")
        config["pm_uninstall"] = pm.strip()
        save_config(config)

        print("Using package manager: ",
        config["pm_uninstall"])
    os.system(f"{config['pm_uninstall']} {package_name}")

def cmd_ping(x):
    try:
        ongoing = subprocess.Popen(f"ping {x}", shell=True)
        ongoing.wait()
    except KeyboardInterrupt:
        ongoing.send_signal(signal.SIGINT)
        ongoing.wait()

def cmd_help():
    print("""
Sparrow PowerShell - Help :
          
          For help with package manager, type "pm-help" in the S-PS

                For More info on commands, check my github repo's COMMANDS.md folder\n
                                            (or)
                 cd Sparrow-PowerShell- for Windows and type *edit code COMMANDS.md*\n
                  cd Sparrow-PowerShell- for Linux and type *edit code COMMANDS.md*
""")
    cwd = os.getcwd()                                   
    open_file_choice = input(f"S-PS {cwd}> y/n: ")
    if open_file_choice == "y":
        text_editor = input(f"S-PS {cwd}> Enter the name of the Text editor you want to use: ")
        os.system(f"{text_editor} COMMANDS.md")
    elif open_file_choice == "n":
        pass

commands = {
    "help" : cmd_help,          "pm-help" : cmd_pm_help,        "echo" : cmd_echo,       "cls" : cmd_cls,
    "del" : cmd_del,            "New-Item" : cmd_newitem,       "time" : cmd_time,       "ls" : cmd_ls,     "pwd" : cmd_pwd,
    "cd" : cmd_cd,              "gc" : cmd_gc,                  "calc" : cmd_calc,       "edit" : cmd_edit, "pip" : cmd_pip,
    "install" : cmd_Install,    "uninstall" : cmd_Uninstall,    "ping" : cmd_ping
}
while True:                                                 
    try:                                                    
        cwd = os.getcwd()                                   # Checks for && seperator and splits UserInput
        UserInput = input(f"\nS-PS {cwd}> ")                # The split list is then iterated and functions are called
        Input = UserInput.split()
        if "&&" in UserInput:
            no_of_commands = UserInput.split('&&')              
            for cmd in no_of_commands:                             # Here, tokens are the individual split commands
                tokens = cmd.strip().split()                       # Which are then called (tokens, as in individual characters like keywords etc)
                if tokens[0] in commands:                          # But here, tokens are the individual commands split from cmd 
                    if len(tokens) > 1:
                        commands[tokens[0]](" ".join(tokens[1:]))     
                    else:                                           
                        commands[tokens[0]]()                        
                elif tokens[0] == "exit":
                    break
                elif tokens[0] not in commands:
                    os.system(UserInput) 

        elif "&&" not in UserInput:
            if Input[0] in commands:                            # The first token of input checking 
                if len(Input) > 1:
                    commands[Input[0]](" ".join(Input[1:]))     # If input > 1, it adds the Input[1] token in parentheses beside the Input[0], Basically a function call
                else:                                           # input[1:] is slicing, Excludes input[0] and joins the rest to the initial function call
                    commands[Input[0]]()                        # If it's not >1, it just becomes the function call.
            elif Input[0] == "exit":
                break
            elif Input[0] not in commands:
                os.system(UserInput)
            else:
                print(f"No such command as {UserInput} Exists.")   # Error exception
    except Exception as e:
        print(f"Error: \n{e}")
