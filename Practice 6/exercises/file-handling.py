#read and print 
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)









#create a text file and write
with open("sample.txt", "w") as file:
    file.write("Hello, this is sample data.\n")
    file.write("This is the second line.\n")

#append new lines
with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")








import shutil
import os

#copy file
shutil.copy("sample.txt", "sample_copy.txt")

#delete file safely
if os.path.exists("sample_copy.txt"):
    os.remove("sample_copy.txt")
    print("File deleted successfully")
else:
    print("File does not exist")