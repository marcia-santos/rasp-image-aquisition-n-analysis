import picamerax as px
from time import sleep
import time
from gpiozero import Button, LED
import ProcessNUpload as pu
import ProcessVideo as pv


btn = Button(2)
led = LED(17)
ir = LED(27)

recording_len = 10

cam = px.PiCamera()
cam.sensor_mode=2
cam.resolution=(1920,1080)
cam.exposure_mode = "night"
cam.awb_mode = "greyworld"

#cam.resolution = (1296,972)

ir.off()
led.off()
    
while(1):
    btn.wait_for_press()
    print("Button was pushed!")
    
    ir.on()
    led.on()
    
    vid = (time.strftime("%y%b%d_%H:%M", time.localtime()))
    
    vid_name = "video_"+vid+".h264"
    cam.start_recording(vid_name)
    cam.wait_recording(recording_len)
    cam.stop_recording()
    
    led.off()
    ir.off()
    
    print("Video Recorded!")
    
    pv.ProcessVideo(vid_name)
    pu.UploadData()

