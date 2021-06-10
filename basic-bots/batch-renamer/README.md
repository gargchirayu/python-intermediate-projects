# Batch Renamer

This python script renames each file in any particular folder as specified (or in its own directory, if not specified), to any filename as provided and increments a count in the filename, for example, Text 1, Text2, so on. If unspecified, it will default to "File 1". The script can be directly run from the terminal, using the following command:

 % python rename_dir.py
 
with optional arguments as:

  -h, --help   show this help message and exit
  --path PATH  Path to folder where files are to be renamed
  --name NAME  Name to be used for renaming. Eg. 'Name'
  

Example: to rename in 'Downloads', with name 'Downloaded-Item'

python rename_dir.py --path /Users/%USERNAME%/Downloads --name Downloaded-Item
