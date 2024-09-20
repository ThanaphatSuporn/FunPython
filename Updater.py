import requests
import os
import shutil

# URL of the GitHub repository raw content
BASE_URL = "https://raw.githubusercontent.com/ThanaphatSuporn/FunPython/main/"

# List of files to update (excluding 'Updater.py')
FILES_TO_UPDATE = ["verison.txt", "fun.py", "Updater.py"]  # Replace with actual script filenames

def download_file(file_name):
    url = BASE_URL + file_name
    response = requests.get(url)
    
    # Check if the file was downloaded successfully
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Updated {file_name} successfully.")
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")

def update_files():
    for file_name in FILES_TO_UPDATE:
        # Skip the updater file
        if file_name == "Updater.py":
            continue
        download_file(file_name)

if __name__ == "__main__":
    print("Checking for updates...")
    update_files()
