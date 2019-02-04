import os
import shutil
import datetime

log = open("image.log", "a+")

pathToImages = os.path.join("C:\\", "Users", "<USERNAME>", "Pictures", "Camera Uploads from Dropbox", "pic-test")

os.chdir(pathToImages)
files = os.listdir(".")

for file in files: 
    # get file name
    filename = os.path.basename(file)
    log.write(f"Filename: {filename}\n")

    # get the time stamp of the image
    timestamp = filename.split(" ")[0]
    log.write(f"Timestamp: {timestamp}\n")

    # directory to make based on the timestamp
    dirToCreate = os.path.join(pathToImages, timestamp)
    log.write(f"Directory to Create: {dirToCreate}\n")

    # if the timestamp folder that we want to create does not already exists
    if not os.path.isdir(dirToCreate):
        # make the directory
        log.write(f"Directory does not already exist, so creating one with path: {dirToCreate}\n")
        os.mkdir(dirToCreate)
    
    # add the current file to the directory
    oldPath = os.path.join(pathToImages, filename)
    log.write(f"Moving image from {oldPath} to {dirToCreate}\n")

    # move the file
    shutil.move(oldPath, dirToCreate)
    log.write("Moving to next file.\n")

log.write("End of directory.\n")