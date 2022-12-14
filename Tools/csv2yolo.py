from imageRotator import points2yolo
import csv
def getCSVpoints(filename):
    lines = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        currentImg = ""
        currentAnn = ""
        for row in csv_reader:
            if line_count == 0:
                print("Leyendo las columnas...")
                line_count+=1
            else:
                imgname = row[0].split(".")[0]
                width = int(row[1])
                height = int(row[2])
                xmin = int(row[3])
                ymin = int(row[4])
                xmax = int(row[5])
                ymax = int(row[6])

                if(currentImg != imgname):
                    print('annotations/{}.txt'.format(imgname))
                    with open('annotations/{}.txt'.format(imgname), 'w') as f:
                        f.write(currentAnn)
                    currentImg = imgname
                    currentAnn = ""
                else:
                    currentAnn += points2yolo([[xmin,ymin],[xmax,ymin],[xmax,ymax],[xmin,ymax]],[width,height])


getCSVpoints("bbox_train.csv")


