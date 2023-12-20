#Import Path and Shutil Modules
from pathlib import Path
import shutil

# Path object that represents the current working directory
current_directory = Path.cwd()
print("Current Directory:", current_directory)

# Create new folder
new_folder_path = current_directory / "folder_week11"
new_folder_path.mkdir()

# Create a path for the "week11.txt" file inside the "folder_week11" directory
text_file_path = new_folder_path / "week11.txt"

# Create a blank file
text_file_path.touch()

# Write text to the file
text_to_write = "Test: Writing to file."
with open(text_file_path, 'w') as file:
    file.write(text_to_write)

# Print the file contents to confirm the text was written
with open(text_file_path, 'r') as file:
    file_contents = file.read()
    print("File Contents:", file_contents)

# Create a new directory inside the directory
backup_directory = new_folder_path / "file_backups"
backup_directory.mkdir()

# Copy the file to the backup file in the "file_backups" directory
shutil.copy(text_file_path, backup_directory / "week11_backup.txt")

# Print out only the txt files in the directory and subdirectories
txt_files = list(new_folder_path.rglob('*.txt'))
print("TXT Files in directory and subdirectories:")
for file in txt_files:
    print(file)