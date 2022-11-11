import shutil
import os
from classChanger import classChanger

def mergeDatasets(datasetA, datasetB):
    destDataset = datasetA+datasetB.split("/")[-1]

    shutil.copytree(datasetB, destDataset)

    destDatasetTest = destDataset + "/test/"
    classChanger(destDatasetTest + "*.txt")

    destDatasetTrain = destDataset + "/train/"
    classChanger(destDatasetTrain + "*.txt")

    aDatasetTest = datasetA+"/test/"
    aDatasetTrain = datasetA+"/train/"

    for file in os.listdir(aDatasetTest):
        shutil.copy(aDatasetTest + file, destDatasetTest)

    for file in os.listdir(aDatasetTrain):
        shutil.copy(aDatasetTrain + file, destDatasetTrain)

datasetA = "/Users/mentxaka/Github/TK-Datasets/Caras"
datasetB = "/Users/mentxaka/Github/TK-Datasets/Matriculas"
mergeDatasets(datasetA,datasetB)
