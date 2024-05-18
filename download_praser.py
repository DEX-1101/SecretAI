import argparse
import os
import subprocess
from tqdm import tqdm

def download_file_with_aria2(url, save_dir='.'):
    local_filename = os.path.join(save_dir, url.split('/')[-1])
    
    # Build the aria2c command
    command = [
        'aria2c',
        '--dir', save_dir,
        '--out', local_filename,
        '--console-log-level=error',
        '--summary-interval=0',
        url
    ]
    
    # Start the aria2c process
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Use tqdm to show a progress bar
    with tqdm(total=100, unit='%') as pbar:
        while True:
            output = process.stderr.readline().decode()
            if process.poll() is not None:
                break
            if output:
                # Extract the percentage complete from the output
                if "DL:" in output and "%" in output:
                    percent_complete = float(output.split('%')[0].split()[-1])
                    pbar.n = percent_complete
                    pbar.refresh()
    
    process.wait()  # Ensure the process has completed
    
    if process.returncode == 0:
        print(f"Downloaded file saved as {local_filename}")
    else:
        print(f"Download failed for: {url}")

def download_from_link_file(link_file_path):
    with open(link_file_path, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip()
        if url:  # Skip any blank lines
            download_file_with_aria2(url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download files from URLs.")
    parser.add_argument("--url", type=str, required=True, help="The URL of the link file to download.")
    parser.add_argument("--config", type=str, help="The URL of the config file to download.")
    
    args = parser.parse_args()
    
    # Step 1: Download the link file
    download_file_with_aria2(args.url)
    link_file_path = os.path.join('.', args.url.split('/')[-1])
    
    # Step 2: Download files listed in the link file
    download_from_link_file(link_file_path)
    
    if args.config:
        config_save_dir = '/kaggle/working/config'
        if not os.path.exists(config_save_dir):
            os.makedirs(config_save_dir)
        download_file_with_aria2(args.config, config_save_dir)
