# Download-zip-uri using python
## URI to CSV Extractor
This Python script facilitates the download and extraction of zip files from specified URIs, saving the extracted contents as CSV files. This is particularly useful for automating the process of fetching data from multiple remote sources.
## How it Works
The script employs the requests library to fetch the zip file content from a given URI. It then saves this content as a zip file in a specified folder and proceeds to extract its contents. The downloaded zip file is subsequently removed to maintain a clean workspace. The script is designed to handle multiple URIs, iterating through a list of provided URLs.
Here's an explanation of the code:
## Importing Libraries:
import requests: Used for making HTTP requests to download content from the URI.
import os: Used for working with the file system, creating directories, and handling file paths.
import zipfile: Used for working with zip files.
## Function: download_and_extract_zip(uri, extracted_folder)
This function takes a URI and a folder path as parameters.
It uses the requests library to get the content of the zip file from the URI.
It then saves the content as a zip file in the specified folder.
The zip file is then extracted into the same folder.
The downloaded zip file is removed to clean up space.
A success message is printed.
## Main Function: main()
Defines a list of zip file URIs (zip_url).
Specifies the folder where the contents of the zip files will be extracted (extracted_folder).
Creates the extracted_folder if it doesn't exist.
Iterates over each URI in the list and calls the download_and_extract_zip function.
## Conditional Execution:
The if __name__ == "__main__": block ensures that the main function is executed when the script is run directly (not when it's imported as a module).


