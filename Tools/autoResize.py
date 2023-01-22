import os
import cv2

def resize_images(folder_path, override=False):
    for filename in os.listdir(folder_path):
        #Check if the file is an image
        if not (filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png")):
            continue
            
        # Open the image
        im = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_UNCHANGED)

        # Crop the image to a 512px square
        height, width = im.shape[:2]
        if width > height:
            difference = width - height
            im = im[:, difference // 2 : width - difference // 2]
        elif height > width:
            difference = height - width
            im = im[difference // 2 : height - difference // 2, :]

        # Rescale the image to 512x512
        im = cv2.resize(im, (512, 512))

        # Save the image
        if override:
            cv2.imwrite(os.path.join(folder_path, filename),im)
        else:
            cv2.imwrite(os.path.join(folder_path, "R-"+filename),im)

# Example usage:
resize_images("/Users/mentxaka/Desktop", override=True)
