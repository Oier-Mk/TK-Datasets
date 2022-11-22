import os
import glob
import cv2
import numpy as np

def rotate(path):

  # Reading and transforming image
  img_read = cv2.imread(path)

  angle = np.random.randint(360)

  # Adjust the angle
  if angle < -45:
    angle = -(90+ angle)
  else:
    angle = -angle

  # Affine transformation
  h, w = img_read.shape[:2]
  center = (w//2, h//2)

  # Rotation 
  M = cv2.getRotationMatrix2D(center, angle, 1.0)
  rotated = cv2.warpAffine(img_read, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
  
  return rotated

def rotator(path):
    files = glob.glob(path)

    for file in files:
        img = rotate(file)
        i = file[-5]
        new_name = '/'.join(file.split('/')[:-1])+"/biscuit"+str(i)+"r.png"
        print(new_name)

        # Renaming the file
        cv2.imwrite(new_name,img)

path = "/Users/mentxaka/Desktop/Stable diffusion/Biscuits/Formateadas/*"
rotator(path)
