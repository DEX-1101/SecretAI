import subprocess

def execute_command_silently(command, message, success_count, failure_count):
    """
    Function to execute a shell command silently.
    """
    try:
        # Run the command in the subprocess silently
        subprocess.run(command, check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{message} '{command}' installed successfully.")
        success_count += 1
    except subprocess.CalledProcessError as e:
        print(f"Error installing '{command}': {e}")
        failure_count += 1
    return success_count, failure_count

if __name__ == "__main__":
    # List of commands with custom messages
    commands = [
        ("apt-get install lz4", "LZ4 package"),
        ("pip install -q colorama", "Colorama package"),
        ("curl -s -OL https://github.com/DEX-1101/sd-webui-notebook/raw/main/res/new_tunnel", "New Tunnel"),
        ("tar -xzf zrok_0.4.23_linux_amd64.tar.gz", "Zrok package")
    ]
    
    # Initialize counters
    success_count = 0
    failure_count = 0
    
    # Execute each command silently with custom messages
    for command, message in commands:
        success_count, failure_count = execute_command_silently(command, message, success_count, failure_count)
    
    # Print summary
    print(f"\nTotal commands installed successfully: {success_count}")
    print(f"Total commands failed to install: {failure_count}")
