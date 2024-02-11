import subprocess
import time

def execute_command_silently(command, message, success_count, failure_count):
    """
    Function to execute a shell command silently.
    """
    start_time = time.time()
    try:
        # Run the command in the subprocess silently
        subprocess.run(command, check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{message} '{command}' installed successfully.")
        success_count += 1
    except subprocess.CalledProcessError as e:
        print(f"Error installing '{command}': {e}")
        failure_count += 1
    end_time = time.time()
    return success_count, failure_count, end_time - start_time

if __name__ == "__main__":
    # List of commands with custom messages
    commands = [
        ("apt-get install lz4", "LZ4 package"),
        ("pip install -q colorama", "Colorama package"),
        ("curl -s -OL https://github.com/DEX-1101/sd-webui-notebook/raw/main/res/new_tunnel", "New Tunnel"),
        ("tar -xzf zrok_0.4.23_linux_amd64.tar.gz", "Zrok package")
    ]
    
    # Initialize counters and total time
    success_count = 0
    failure_count = 0
    total_time = 0
    
    # Execute each command silently with custom messages
    for command, message in commands:
        success_count, failure_count, command_time = execute_command_silently(command, message, success_count, failure_count)
        total_time += command_time
    
    # Print summary
    print(f"\nExecuted command: {success_count}, Error: {failure_count}, All completed within: {total_time:.2f} seconds")
