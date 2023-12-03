# cpFileNameToTitle
This is a python script is intended for Windows systems. This script will copy the file name of a video file and apply it to the title in the meta data.

# Purpose
My family backs up all our dvds on a windows machine and we use that drive to stream all those videos to our smart devices in the house. One exception is our main tv room where there is an apple tv. I could run iTunes on the windows machine and share the backup drive with the apple tv. This would eliminate the rest of the family having to ask us to put movies on for them. There was one problem: iTunes displays the title of the file from the metadata and not the file name. This script was created to automate the task of copying the file name of each video file and pasting it into the 'title' metadata of the file.

# Setup
This script repires the **mutagen** and **pywin32** libraries. Yo ucan install them by typing the following into your command prompt:
```
pip install mutagen
pip install pywin32
```

***IMPORTANT:*** Before running the script, ensure every file in your directory **is not** in *read only* mode. Simply navigate to the parent of the directory you want to affect. Right click on your directory and select *Properties*. In the properties window, make sure *Read Only* is **not** checked. If it is, uncheck it and click *ok*. You will be prompted if you would like to make these changes to the file only or to all subfolders and files; select all subfolders and files and click *ok*.

Once those dependencies are installed, and you have ensured all files **are not** in *read only* mode, navigate to the parent directory of the script and run it by entering into the command line:
```
python cpFileNameToTitle.py
```
You will be prompted for the URL of the folder containing the video file(s) you want to change:
```
Enter your media folders path: C:\Your\Video\Folder
```
Once entered, the script will crawl through the folder and all subfolders and change the title in the metadata from whatever it is to its file name. If the title attribute is missing from the file, this will add the attribute with the value of "1" and then change it to the desired value.

**NOTE:** If there are any other types of files in the directory or any of the subdirectories, the script will terminate. This will be fixed with future iterations.
