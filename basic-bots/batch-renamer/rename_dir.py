import os
import argparse

parser = argparse.ArgumentParser(
    description="Renames all file in a directory, with name specified"
)

parser.add_argument(
    "--path", type=str, default='.', help="Path to folder where files are to be renamed"
)

parser.add_argument(
    "--name", type=str, default='File', help="Name to be used for renaming. Eg. 'Name'"
)

args = parser.parse_args()
if args.path == '.':
    path = os.getcwd()
else:
    path = args.path

name = args.name

print("Renaming in directory", path)
counter = 1

for file in os.listdir(path):
    if os.path.isfile(path + '/' + file):
        file_name, file_ext = os.path.splitext(file)
        if file_name == 'rename_dir' or file_name.startswith('.'):
            continue
        old_name = path + '/' + file_name
        new_name = path + '/' + name + " " + str(counter)
        os.rename(old_name + file_ext, new_name + file_ext)
        counter += 1
