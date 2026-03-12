#this example is more a propblem set in a test and the use of the packages of python does makes more easy to work on those

import os
import shutil
import tarfile

# Source and destination directories
source_dir = "/logs"
dest_dir = "/etc"

# Backup file extensions
backup_extensions = (".bak", ".backup", ".old", ".bkp")

# List to store moved files
moved_files = []

# Step 1: Read files in /logs
for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)

    # Step 2: Check if it is a backup file
    if os.path.isfile(file_path) and file.endswith(backup_extensions):

        # Destination path
        dest_path = os.path.join(dest_dir, file)

        # Step 3: Move file
        shutil.move(file_path, dest_path)

        moved_files.append(dest_path)
        print(f"Moved: {file} -> {dest_dir}")

# Step 4: Create tar.gz archive of moved files
tar_path = os.path.join(dest_dir, "backup_files.tar.gz")

with tarfile.open(tar_path, "w:gz") as tar:
    for file in moved_files:
        tar.add(file, arcname=os.path.basename(file))

print(f"Archive created: {tar_path}")