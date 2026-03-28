import os

#create nested directories
os.makedirs("test_dir/sub_dir", exist_ok=True)

#list files and directories
items = os.listdir(".")
print("Files and directories:", items)

#find files by extension
for file in items:
    if file.endswith(".txt"):
        print("Text file:", file)








import shutil

#move file to directory
shutil.move("sample.txt", "test_dir/sample.txt")

#copy file back
shutil.copy("test_dir/sample.txt", "sample.txt")