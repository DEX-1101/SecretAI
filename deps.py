import subprocess
import time
from colablib.colored_print import cprint, print_line

# ANSI escape codes for text color
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_RESET = "\033[0m"

def kontolondon(command, message, success_count, failure_count):
    """
    Function to execute a shell command silently.
    """
    start_time = time.time()
    print(f"installing {message}")
    try:
        # Run the command in the subprocess silently
        subprocess.run(command, check=True, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #cprint(f"{message}", color="flat_cyan")
        success_count += 1
    except subprocess.CalledProcessError as e:
        print(f"Error installing [ {message} ]: {e}")
        failure_count += 1
    end_time = time.time()
    return success_count, failure_count, end_time - start_time

if __name__ == "__main__":
    # List of commands with custom messages
    commands = [
        
        ("apt -y install -qq aria2", "aria2"),
        ("apt-get install lz4", "lz4"),
        ("pip install -q colorama", "colorama"),
        ("npm install -g localtunnel", "localtunnel"),
        ("curl -s -OL https://github.com/DEX-1101/sd-webui-notebook/raw/main/res/new_tunnel", "new_tunnel"),
        ("curl -s -Lo /usr/bin/cl https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 && chmod +x /usr/bin/cl", "cloudflare"),
        ("curl -sLO https://github.com/openziti/zrok/releases/download/v0.4.23/zrok_0.4.23_linux_amd64.tar.gz && tar -xzf zrok_0.4.23_linux_amd64.tar.gz && rm -rf zrok_0.4.23_linux_amd64.tar.gz && mv /kaggle/working/zrok /usr/bin", "zrok")
    
    ]
    
    # Initialize counters and total time
    success_count = 0
    failure_count = 0
    total_time = 0
    
    # Execute each command silently with custom messages
    for command, message in commands:
        success_count, failure_count, command_time = kontolondon(command, message, success_count, failure_count)
        total_time += command_time
    
    # Print summary
    print(f"\n{failure_count} of {success_count} error found. All completed within: {total_time:.2f} secs")
