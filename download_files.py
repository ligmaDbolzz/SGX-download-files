import argparse
import requests
import os
import logging
import datetime

# Set up logging
logging.basicConfig(filename='download.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def download_files(date=None, historical=False):
    # 5489 -> date: 2023/08/21
    base_url = "https://links.sgx.com/1.0.0/derivatives-historical/5489/"
    file_types = ["WEBPXTICK_DT.zip", "TickData_structure.dat", "TC.txt", "TC_structure.dat"]

    # If date is not provided, set it as today
    if date is None:
        date = datetime.datetime.today().strftime('%Y%m%d')

    # Create a folder with the current date to store the downloaded files
    folder_name = f"files_{date}"
    os.makedirs(folder_name, exist_ok=True)

    # Download the files
    for file_type in file_types:
        url = base_url + f"{file_type}"
        res = requests.get(url)

        # If the download is successful, save the file
        if res.status_code == 200:
            file_name = url.split("/")[-1]
            file_path = os.path.join(folder_name, file_name)
            with open(file_path, 'wb') as file:
                file.write(res.content)
                logging.info(f"Downloaded: {file_name}")
        else:
            logging.error(f"Failed to download: {file_type}")
            # Re-download the file if it failed
            retry = input("Do you want to re-download the file? (y/n) ")
            if retry.lower() == 'y':
                res = requests.get(url)
                if res.status_code == 200:
                    file_name = url.split("/")[-1]
                    file_path = os.path.join(folder_name, file_name)
                    with open(file_path, 'wb') as file:
                        file.write(res.content)
                        logging.info(f"Re-downloaded: {file_name}")
                else:
                    logging.error(f"Failed to re-download: {file_type}")

    # If historical flag is True, download older files
    if historical:
        # Logic to download older files
        pass

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='SGX Download Files')
    parser.add_argument('--date', type=str, help='Specify a date (format: "YYYYMMDD") to download files')
    parser.add_argument('--historical', action='store_true', help='Download historical files')
    args = parser.parse_args()

    # Download files based on command line arguments
    download_files(date=args.date, historical=args.historical)