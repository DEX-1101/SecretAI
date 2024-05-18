import argparse
import os
import time
import aria2p
from tqdm import tqdm

def download_file_with_aria2(url, save_dir='.'):
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://localhost",
            port=6800,
            secret=""
        )
    )
    
    download = aria2.add_uris([url], options={"dir": save_dir})
    
    print(f"Starting download: {url}")
    
    # Progress bar initialization
    with tqdm(total=100, unit='%') as pbar:
        while not download.is_complete:
            download.update()
            if download.total_length > 0:
                percent_complete = (download.completed_length / download.total_length) * 100
                pbar.n = percent_complete
                pbar.refresh()
            time.sleep(0.5)  # Update interval
    
    if download.is_complete:
        print(f"Downloaded file saved as {os.path.join(save_dir, url.split('/')[-1])}")
    elif download.has_failed:
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
