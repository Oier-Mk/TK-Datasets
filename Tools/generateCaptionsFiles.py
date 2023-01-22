import os
import glob


#from a folder with images i need to generate a captions file with the name of the image in txt format
def generateCaptionsFile(path):
    files = glob.glob(path)
    name = path.split("/")[-2]
    for i, file in enumerate(files):
        new_name = path[:-1]+name+str(i)+".txt"
        print(new_name)
        # create a txt file with new_name
        open(new_name, "w")

path = "/Users/mentxaka/Desktop/MapsPeople/*"
generateCaptionsFile(path)
