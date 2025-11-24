"""                  SPS Commands loader
This library (more like a singular function) loads all the lib files.
And from those files, loads all the commands. Modular & Supports plugins.
It also hosts the metadata dict for all the commands. The metadata dict can get big, Please don't be scared
"""

import importlib
import os
lib_path = os.path.abspath(os.path.join("S-PS","SPS_Libs"))

def load_commands() -> dict:
    commands = {}
    try:
        for file in os.listdir(lib_path):
            if file.endswith(".py") and file != "__init__.py":
                module_name = f"SPS_Libs.{file[:-3]}"
                mod = importlib.import_module(module_name)

                for attr in dir(mod):
                    if attr.startswith("cmd_"):
                        commands[attr[4:]] = getattr(mod, attr)
        return commands
    except Exception as e:
        print(f"There was an issue importing/creating the function loader.\nError Code :\n\n{e}")
        return commands

def load_metadata() -> dict:
    return {
        "del":"Deletes file or dir specified.",
        "":"",
    }