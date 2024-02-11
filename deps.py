import subprocess

def execute_command(command):
    """
    Function to execute a shell command.
    """
    try:
        # Run the command in the subprocess
        subprocess.run(command, check=True, shell=True)
        print(f"Command '{command}' executed successfully.")
        return True, None
    except subprocess.CalledProcessError as e:
        error_message = f"Error executing command '{command}': {e}"
        print(error_message)
        return False, error_message

if __name__ == "__main__":
    # List of commands to execute
    commands = [
        "apt-get install lz4",
        "pip install -q colorama",
        "curl -s -OL https://github.com/DEX-1101/sd-webui-notebook/raw/main/res/new_tunnel",
        "!apt -y install -qq aria2"
    ]
    
    # Execute each command
    for command in commands:
        success, error_message = execute_command(command)
        if success:
            print(f"Command '{command}' was successfully installed.")
        else:
            print(f"Error occurred while executing command '{command}': {error_message}")

