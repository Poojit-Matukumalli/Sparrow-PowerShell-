import os, shutil
from datetime import datetime

def cmd_ls():       #ls, lists subdirectories
    stdout = []
    a = os.listdir()
    for char in a:
        stdout.append(char)
    return "\n".join(stdout)

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
            return "Cannot remove Critical system files"
        elif os.path.exists(file_path):
            shutil.rmtree(file_path)                            # Well, This is the file deletion segment
            return "Deletion Successful."
        else:
            print(f"File '{file_path}' not found.")
    except PermissionError:
        return "File removal denied. Insufficient Permission level"
    except Exception as e:
        return f"An unexpected error occurred:\n\n{e}"

def cmd_newitem(filename):   #The file creation segment
    if os.name == "nt":
        open(f"{filename}", "w")
        return f"""\nDirectory: {os.getcwd()}\n
Mode           : new item\n
LastWriteTime  : {datetime.now()} \n
Length         : 0\n
name           : {filename}\n"""
    else:
        os.system(f"touch {filename}")
        print( "Mode           : Created (touch)\n"
              f"LastWriteTime  : {datetime.now()} \n"
               "Length         : 0\n"
              f"name           : {filename}"
            )
        
def cmd_gc(filename): #gc, Get-Contents
    try:
        with open(filename, "r") as f:
            print(f.read())
    except Exception as e:
        print(f"An error occurred:\n{e}")

def cmd_edit(x):
    os.system(x)
