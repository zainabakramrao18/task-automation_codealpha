import os
import shutil

# Get folder paths from user
source_folder = input("Enter the path of the source folder: ").strip()
destination_folder = input("Enter the path of the destination folder: ").strip()

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move .jpg files
moved_files = 0
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.jpg'):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dst_path)
        print(f'Moved: {filename}')
        moved_files += 1

print(f"\nTotal .jpg files moved: {moved_files}")
