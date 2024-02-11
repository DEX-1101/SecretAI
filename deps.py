import subprocess

# ANSI escape codes for text color
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_RESET = "\033[0m"

def execute_command_silently(command, message, color, success_count, failure_count):
    """
    Function to execute a shell command silently.
    """
    try:
        # Run the command in the subprocess silently
        subprocess.run(command, check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{color}{message} '{command}' installed successfully.{COLOR_RESET}")
        success_count += 1
    except subprocess.CalledProcessError as e:
        print(f"{COLOR_RED}Error installing '{command}': {e}{COLOR_RESET}")
        failure_count += 1
    return success_count, failure_count

if __name__ == "__main__":
    # List of commands with custom messages and colors
    commands = [
        ("apt-get install lz4", "LZ4 package", COLOR_GREEN),
        ("pip install -q colorama", "Colorama package", COLOR_RED),
        ("!curl -s -OL https://github.com/DEX-1101/sd-webui-notebook/raw/main/res/new_tunnel", "New Tunnel", COLOR_GREEN),
        ("tar -xzf zrok_0.4.23_linux_amd64.tar.gz", "Zrok package", COLOR_RED)
    ]
    
    # Initialize counters
    success_count = 0
    failure_count = 0
    
    # Execute each command silently with custom messages and colors
    for command, message, color in commands:
        success_count, failure_count = execute_command_silently(command, message, color, success_count, failure_count)
    
    # Print summary
    print(f"\n{COLOR_GREEN}Total commands installed successfully: {success_count}{COLOR_RESET}")
    print(f"{COLOR_RED}Total commands failed to install: {failure_count}{COLOR_RESET}")
