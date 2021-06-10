import os
import argparse

parser = argparse.ArgumentParser(
    description="Cleans up any folder and segregates according to file type"
)

parser.add_argument(
    "--path", type=str, default='.', help="Path to the folder that is to be cleaned"
)

args = parser.parse_args()
path = args.path

# reading list of items in given directory
content = os.listdir(path)
# joining the path to each file name, so it reads: ./file.txt instead of file.txt
path_content = [os.path.join(path, doc) for doc in content]

# segregating the files and folders in different lists
files = [file for file in path_content if os.path.isfile(file)]
folders = [folder for folder in path_content if os.path.isdir(folder)]

print("Cleaning up", len(files), "of", len(content), "elements")
# counter for moved files
counter = 0
# list of already created folders
created_folders = []

for file in files:
    full_path, ext = os.path.splitext(file)
    file_path = os.path.dirname(full_path)
    file_name = os.path.basename(full_path)

    # print(ext)
    # print(file_name)
    # print(file_path)
    # print(full_path)

    # check for this python script and hidden files
    if file_name == 'cleanup_dir' or file_name.startswith('.'):
        continue
    subfolder = os.path.join(path, ext[1:].lower())

    if subfolder not in folders or subfolder not in created_folders:
        try:
            os.mkdir(subfolder)
            created_folders.append(subfolder)
            print("Created new directory:", subfolder)
        except FileExistsError as error:
            print("File already exists. File moved to path:", subfolder, "(Error:", error, ")")

    new_path = os.path.join(subfolder, file_name) + ext
    os.rename(file, new_path)
    counter += 1

print("Cleanup process completed with", counter, "new subfolders")




