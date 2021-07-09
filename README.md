# rasp-image-aquisition-n-analysis
These files were developed to acquire a video using Raspberry and Rasp Camera in the infrared spectrum, segment the image, and then upload the data on google drive.

# Description of the files

## InitFilesArchive.py
This algorithm sets the file that keeps track of new files in the folder. It must be run before main.py.

## main.py
This algorithm controls image acquisition. It sets algorithm sets the Rasp Camera configuration, records the video, and then calls functions to analyze the signal and upload it to google drive. When the recording starts, a LED is turned on to signal the recording as well as the infrared illumination.
This algorithm depends on the following:

### ProcessVideo.py
This algorithm process the video. It segments the main element of the video and computes the difference over time and save it to a csv.

### ProcessNUpload.py
This algorithm finds what are the new videos and csv on the folder. Then, upload them on Google Drive. 

### GoogleDrive.py
This algorithm identifies the current authorization file or creates a new one before uploading the new files to the cloud.


