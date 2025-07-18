# Task Automation: Move .jpg Files with Python

This is a simple Python automation script that moves all `.jpg` files from a **source folder** to a **destination folder**. The script uses user input to define both paths.

## 🛠️ Key Concepts Used

- `os` — for handling file paths and directories  
- `shutil` — for moving files  
- `file handling` — user interaction and file management  

## 💡 How It Works

1. The script asks the user to enter:
   - Path to the **source** folder (where `.jpg` files are located)
   - Path to the **destination** folder (where `.jpg` files will be moved)

2. If the destination folder doesn’t exist, it is automatically created.

3. The script scans the source folder and moves all files ending with `.jpg` to the destination folder.

4. A summary of moved files is printed at the end.

## 📄 Sample Input

