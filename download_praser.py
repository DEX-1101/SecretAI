import argparse
import os
import requests
from tqdm import tqdm

def download_file(url, save_dir='.'):
    local_filename = os.path.join(save_dir, url.split('/')[-1])

    # Send a GET request to the URL with stream=True
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size = int(r.headers.get('content-length', 0))  # Get the total file size
        chunk_size = 8192
        with open(local_filename, 'wb') as f, tqdm(
            total=total_size, unit='iB', unit_scale=True
        ) as bar:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                bar.update(len(chunk))  # Update the progress bar
    print(f"Downloaded file saved as {local_filename}")
    return local_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download files from URLs.")
    parser.add_argument("--url", type=str, required=True, help="The URL of the file to download.")
    parser.add_argument("--config", type=str, help="The URL of the config file to download.")
    
    args = parser.parse_args()
    
    download_file(args.url)
    
    if args.config:
        config_save_dir = '/kaggle/working/config'
        if not os.path.exists(config_save_dir):
            os.makedirs(config_save_dir)
        download_file(args.config, config_save_dir)
