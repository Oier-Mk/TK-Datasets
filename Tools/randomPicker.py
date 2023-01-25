import random
import shutil
import os

def pick_random_files(src_folder, dest_folder, n):
    files = os.listdir(src_folder)
    random_files = random.sample(files, n)
    for file in random_files:
        src_path = os.path.join(src_folder, file)
        dest_path = os.path.join(dest_folder, file)
        shutil.move(src_path, dest_path)

# Example usage:
pick_random_files("/Users/mentxaka/Downloads/chest_xray/train/PNEUMONIA", "/Users/mentxaka/Downloads/chest_xray/rdmSplit/Pneumonia", 50)
