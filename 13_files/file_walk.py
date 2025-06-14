#GOAL: walk through each file in a dir, to act on each
import os

for folder_name, sub_folders, file_names in os.walk(".\\13_files"): #folder name = 13_files
    #note os.walk returns 3 values per iteration
    print('current folder is ' + folder_name)
    print('subfolders are ' + str(sub_folders))
    print('files are ' + str(file_names))
    print()

#os.join already inserts an appropriate \ or / for you eg. os.join(folder + file)