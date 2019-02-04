# Moving file from Dropbox to a different directory

## Description

### I use Dropbox to upload my pictures/videos from my phone to my computer since my iPhone refuses to import over 1500 pictures/videos from my phone. So all the pictures from Dropbox goes to a certain directory and saves the image/video there on my computer. The format that it uploads it as is always the same i.e. YYYY-mm-dd and a number that I'm not sure where comes from (13.03.53) and adds the file extension. 

### So I created this very simple script to learn more about Python while helping organize my pictures into their own folder by date. It basically just strips the date from the image, if the directory doesn't exist then create it and move the file from the old Dropbox path to the new folder that was just created. This allows me to free up space in Dropbox since I only have 2GB.

## Future Updates

### I want to set this up with my task scheduler on Windows, so that any time the Dropbox folder is updated or changed, then I want to run this script, so the new file goes from Dropbox to the correct folder in my new directory. 

### I haven't integrated this with videos yet, but it shouldn't be difficult. I just have to move it from Dropbox to my uploads/videos/ directory and my pictures go to uploads/pictures/ directory.

### Not sure what else I can do with it, but I'm sure I'll come up with something.