import subprocess

def cmd_ping(x):
    try:
        ongoing = subprocess.run(["ping", x], capture_output=True, text=True)
        return ongoing.stdout
    except Exception as e:
        return f"Error while pinging service.\nError:\n{e}"
    except KeyboardInterrupt:
        return 
    