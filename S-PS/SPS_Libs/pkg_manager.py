import os, json, subprocess, sys

def cmd_pip(package_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        return f"\n\n{'-'*120}\n{package_name} installed successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to install {package_name}. error:\n{e}"
    except Exception as e:
        return f"An error occoured during install.\nError:\n{e}"
    

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
    
