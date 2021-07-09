import pandas as pd
import os
import GoogleDrive as GD

def UploadData():
    files=pd.read_csv('files.csv')
    list_of_files=os.listdir()

    if len(files.files)!= len(list_of_files):
        
        #identify new videos
        list_new_videos = list(set(list_of_files)-set(files.files))
        for x in list_new_videos:
            if x.find(".h264") != -1:
               #process_video(x)
               GD.Upload("video/H264", x)
            elif x.find("csv") != -1:
                GD.Upload("text/csv", x)
            
               
               
        
        #apend the new files and save the files.csv again
        list_of_files=list(set(list_of_files))
        pd.DataFrame({'files':list_of_files}).to_csv('files.csv')
        
        
