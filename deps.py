import subprocess

# ANSI color escape codes
class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

def execute_command_silently(command, message, color):
    """
    Function to execute a shell command silently.
    """
    try:
        # Run the command in the subprocess silently
        subprocess.run(command, check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{color}{message} '{command}' installed successfully.{Color.RESET}")
    except subprocess.CalledProcessError as e:
        print(f"{Color.RED}Error installing '{command}': {e}{Color.RESET}")

if __name__ == "__main__":
    # List of commands with custom messages and colors
    commands = [
        ("apt-get install lz4", "LZ4 package", Color.GREEN),
        ("pip install -q colorama", "Colorama package", Color.GREEN),
        ("curl -s -OL https://github.com/DEX-1101/sd-webui-notebook/raw/main/res/new_tunnel", "New Tunnel", Color.GREEN),
        ("!tar -xzf zrok_0.4.23_linux_amd64.tar.gz", "Zrok package", Color.GREEN)
    ]
    
    # Execute each command silently with custom messages and colors
    for command, message, color in commands:
        execute_command_silently(command, message, color)
