from os import access
import cv2

import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):

        ret,frame=videoCaptureObject.read()
        img_name="Img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("Snap Shot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token='sl.BGdaxzdL0tbkWT7cv8W_gSll4ubBCPeS-9GljP5pLHL2SnuAOIgeCktF3jWB1Er1lK93qIWHH9Duo-fDYNVRYc_YSFUb9o8TtNip7PzPWv11c2149415p5TNQ-GRjK0v17qxMDZqJQSu'
    file=img_name
    file_from=file
    file_to="/testfolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file Uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()