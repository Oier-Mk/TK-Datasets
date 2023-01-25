#delete those files L2 or R2 is on the name

import os
import glob
import shutil

#function to delete files with L2 or R2 on the name
def deleter(path):
    n = 0
    files = glob.glob(path)
    for file in files:
        #if clause to check if the file has L2 or R2 on the name
        if "L2" in file or "R2" in file:
            #deleting the file
            n += 1
            os.remove(file)
            print(file)

#function to split in 2 folders L and R on the name of the file
def splitter(path):
    if not os.path.exists(path[:-1]+"L") and not os.path.exists(path[:-1]+"R"):
        #create the L and R folders taking into account the given path
        os.mkdir(path[:-1]+"L")
        os.mkdir(path[:-1]+"R")
    files = glob.glob(path)
    for file in files:
        #if clause to check if the file has L or R on the name
        if "L" in file:
            #change directory of the file to the folder with L with shutil
            shutil.move(file, path[:-1]+"L")
        elif "R" in file:
            #change directory of the file to the folder with R with shutil
            shutil.move(file, path[:-1]+"R")

path = "/Users/mentxaka/Desktop/Arms/*"
deleter(path)
splitter(path)


from ultralytics import YOLO

# Load a model
model = YOLO("path/to/best.pt")  # load a custom model

#function that predicts with the images of a folder given the path and the loaded model throw parameter
def predictor(path, model):
    files = glob.glob(path)
    for file in files:
        results = model(file)
        print(results)


# Predict with the model
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image


#move file from one folder to another
