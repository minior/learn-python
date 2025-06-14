import os
import shutil

print('Working dir is ' + os.getcwd()) # gets current working dir for relative file paths
#.\ means this folder, ..\ means parents folder

# os.chdir("target dir")    -> to change working dir
# os.listdir                -> lists all files and folders in current dir

hellofile = open(r"C:\Users\mrmin\Documents\Coding\Python\13_files\hellofile.txt")
print(hellofile.read())

#use keyword args "w" or "a" for rewrite or append mode
hellofile = open(r"C:\Users\mrmin\Documents\Coding\Python\13_files\hellofile.txt", "a")
#will create a new file if it doesnt already exist

# os.unlink('target')   -> delete file
# os.rmdir('target')    -> delete folder ONLY IF EMPTY

#shelves are like dictionaries, binary files ie. not plain text
import shelve
shelf_file = shelve.open('13_files\\shelftest')
shelf_file['ranks'] = ['gremlin', 'imp', 'wizard', 'warlock'] # writes this info
print(list(shelf_file.keys()))      #['ranks']
print(list(shelf_file.values()))    #[['gremlin', 'imp', 'wizard', 'warlock']]

#using shutil
import shutil 

shutil.copy(".\\13_files\\hellofile.txt", ".\\13_hellofilecopy.txt") #(source, dest+rename)

# shutil.copytree("source", "dest")     -> to copy a folder:
# shutil.move("source","dest")          -> move

# shutil.move("source","dest\\new_name.txt") -> RENAMES

# shutil.rmtree('target')               -> deletes folder REGARDLESS if empty
# so good to do a print "dry run"
for file in os.listdir(): #all files and folders in current dir
    if file.endswith(".txt"):
        #os.unlink(file)    -> make deleting actions a comment first
        print(file)         # avoid deleting in case of typo




