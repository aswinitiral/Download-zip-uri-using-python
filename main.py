import requests
import os
import zipfile

# Function to download and extract zip content from a URI
def download_and_extract_zip(uri, extracted_folder):
    response = requests.get(uri)
    if response.status_code == 200:
        # Extract filename from URI
        filename = os.path.join(extracted_folder, os.path.basename(uri))
        # Save the content as a zip file
        with open(filename, 'wb') as file:
            file.write(response.content)
        # Extract the contents of the zip file
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)
        # Remove the downloaded zip file
        os.remove(filename)
        # Print a success message
        print(f"Downloaded, extracted, and deleted zip file: {uri}")
    else:
        print(f"Failed to download and extract: {uri}")

def main():
    # Replace 'your_zip_url' with the actual URL of your zip file
    zip_url = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
    ]
    extracted_folder = 'extracted_files'
    # Create a folder to extract files
    os.makedirs(extracted_folder, exist_ok=True)
    # Iterate over URIs and download/save CSV content
    for uri in zip_url:
        download_and_extract_zip(uri, extracted_folder)

if __name__ == "__main__":
    main()


