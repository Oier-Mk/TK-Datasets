import os
import glob

def renamer(path):
    files = glob.glob(path)
    name = path.split("/")[-2]

    for i, file in enumerate(files):

        new_name = path[:-1]+name+" ("+str(i)+").png"

        # Renaming the file
        os.rename(file, new_name)  

path = "/Users/mentxaka/Downloads/WholeBiscuits24012023/*"

renamer(path)





