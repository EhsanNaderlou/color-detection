# print("fuck this world :) ")
import cv2
import numpy as np
from joblib import load
from tkinter import *

def NotFindWindow():
    windows = Tk()
    windows.maxsize(250,100)
    windows.minsize(250,100)
    frame = Frame(windows)
    t1 = Label(frame , text="the camera is not find !" , font=(10,10,"bold"))
    b1 = Button(frame , text="QUIT" , command= lambda : windows.destroy())
    frame.pack(pady=20)
    t1.grid(column=0 , row=0)
    b1.grid(column=0, row=1 , pady=5)
    windows.mainloop()


model = load("./model/model.joblib") # load the model
camera = cv2.VideoCapture(0) # load the camera
show = True

while show :
    _ , img = camera.read()
    # if the camera was avaliable
    if _ :
        # video resolution
        y , x = img.shape[:2]

        # the center pixel
        pixel_bgr = img[-int(y/2) , -int(x/2)]
        rgb = f"RGB : {pixel_bgr[::-1]}" # RGB

        # convert the rgb to hex code
        RgbToHex = lambda r,g,b: '#{:02x}{:02x}{:02x}'.format(r, g, b)
        hex_code = f"Hex : {RgbToHex(pixel_bgr[2] , pixel_bgr[1] , pixel_bgr[0])}"

        # model color predict
        predict = f"Color : {model.predict(np.array([pixel_bgr[::-1]]))[0]}"

        # draw on screen
        cv2.rectangle(img , (13 , 10) , (80 , 30) , [int(pixel_bgr[0]) ,int(pixel_bgr[1]) ,int(pixel_bgr[2])]  , -1)
        cv2.putText(img, "press the Q to quit" , (int(x/2)-140 , y-30) ,cv2.FONT_HERSHEY_SIMPLEX , 0.8 , (0,0,255) , 1 )
        cv2.putText(img, rgb , (13 , 55) ,cv2.FONT_HERSHEY_SIMPLEX , 0.6 , (0,0,0) , 1 )
        cv2.putText(img, hex_code , (13 , 80) ,cv2.FONT_HERSHEY_SIMPLEX , 0.6 , (0,0,0) , 1 )
        cv2.putText(img , predict , (13 , 100) , cv2.FONT_HERSHEY_SIMPLEX , 0.6 , (0,0,0) , 1)
        cv2.circle(img , (int(x/2) , int(y/2)) , 3 , (0,255,0) , -1)

        cv2.imshow("image" , img) # display the camera
        #exit
        if cv2.waitKey(30) == ord("q") :
            cv2.destroyAllWindows()
            show = False

    # if the camera wasn't avaliable
    else :
        show = False # stop the while loop
        NotFindWindow() # the window that show to the user , they camera is not avaliable
