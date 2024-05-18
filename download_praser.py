import argparse
import requests

def download_file(url):
    # Get the filename from the URL
    local_filename = url.split('/')[-1]
    
    # Send a GET request to the URL
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        # Open a local file with the same name as the URL's file
        with open(local_filename, 'wb') as f:
            # Write the contents of the response to the local file
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded file saved as {local_filename}")
    return local_filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a file from a URL.")
    parser.add_argument("--url", type=str, required=True, help="The URL of the file to download.")
    
    args = parser.parse_args()
    
    download_file(args.url)
