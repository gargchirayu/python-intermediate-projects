# Directory Cleanup

This programs cleanups a directory, that is, segregates all files in any folder as specified (or in its own directory, if not specified) into subsequent folders, named as the file extension, in the same directory. For example, PDFs are stored in a new folder named "pdf", TXTs go into folder "txt", and so on. Using a simple if-else block, the same can also be implemented into file types like Documents, Packages, Applications, etc; but I haven't implemented that for now. 

The script can be directly run from the terminal, using the following command:

% python cleanup_dir.py

with optional arguments as:
-h, --help   show this help message and exit
--path PATH  Path to the folder that is to be cleaned

Example: to cleanup the 'Downloads' folder
python cleanup_dir.py --path /Users/%USERNAME%/Downloads
