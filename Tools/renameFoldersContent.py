import os
import glob

def renamer(path):
    files = glob.glob(path)

    for i, file in enumerate(files):
        print(i)
        print(file)
        print(path[:-1]+"Picture"+str(i)+".png")

        new_name = path[:-1]+"Picture"+str(i)+".png"

        # Renaming the file
        os.rename(file, new_name)  

path = "/Users/mentxaka/Desktop/Stable diffusion/Originales/*"
renamer(path)
