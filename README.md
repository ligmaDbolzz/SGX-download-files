# Project Name: SGX Download Files

## Description

This project is a Python script that allows you to download specific files related to SGX (Singapore Exchange) derivatives data. It provides functionality to download files for a specific date or historical files.

## Prerequisites

To run this project, you need to have Python installed on your system.

## Installation

1. Clone the repository from GitHub: [repository URL]

2. Navigate to the project directory.

3. Install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

## Usage

To run the script, open a terminal or command prompt and navigate to the project directory.

Run the following command:

```
python sgx_download_files.py [--date <date>] [--historical]
```

- `--date`: (optional) Specify a specific date in the format "YYYYMMDD" to download files for that date. If not provided, files for the current date will be downloaded.

- `--historical`: (optional) Include this flag to download historical files. This will download additional files based on the logic specified in the script.

## Logging

The script logs its activities to a file named `download.log` using the `logging` module. The log file will be created in the same directory as the script.

## File Structure

The downloaded files will be stored in a folder named `files_<date>`, where `<date>` represents the date for which the files were downloaded. The folder will be created in the same directory as the script.

## Error Handling

If a file fails to download, the script logs an error and prompts you to re-download the file. You can choose to re-download the file by confirming with `y` or `n` to skip the file.

## Contributing

If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

Feel free to customize and expand upon this project according to your needs.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This project was inspired by the need to download specific SGX derivatives files efficiently.

[Optional: Add any acknowledgments or credits to individuals or resources that assisted with the development of the project.]

## Disclaimer

[Include any disclaimers or legal notices as necessary.]

Happy downloading! 😄📂

