import os
import shutil

path = input("Enter the path of the folder to organize:\n>> ").strip()

if not os.path.exists(path):
    print("Path does not exist.")
    exit()

extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".c", ".sh", ".bat"],
    "Others": []
}

files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

if not files:
    print("No files to organize.")
    exit()

for file in files:
    moved = False
    file_ext = os.path.splitext(file)[1].lower()
    for folder, exts in extensions.items():
        if file_ext in exts:
            folder_path = os.path.join(path, folder)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(os.path.join(path, file), os.path.join(folder_path, file))
            moved = True
            break
    if not moved:
        folder_path = os.path.join(path, "Others")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

print("Files organized successfully!")
