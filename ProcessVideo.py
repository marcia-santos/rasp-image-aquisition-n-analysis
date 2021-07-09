# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 23:45:31 2021

@author: Márcia Santos Inspirado em Gabriela Coppeti e Jean Schimit
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import imutils as imutils
import cv2


def ProcessVideo(file_name):

    ##criar tabela para colocar frames
    df = pd.DataFrame(columns=[ 'Total', '1', '0'])

    ##Abrir Video
    video = cv2.VideoCapture(file_name)

    if not video.isOpened():
        print("Error opening video stream or file") 

    ## Criar Matrix para resultado



    ##Pegar primeiro frame e criar uma mascara para padronizar região.

    #ler frame para mask
    ret, frame = video.read()

    #cortar na regiçao do sensor
    frame = frame[0:1080,0:650]


    #Criar mascara.
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(frame, (1, 1), 0)
    thresh, mask = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY )    
    #plt.imshow(mask, cmap="gray")
    #plt.show()

    total = 1080*650
    i=0
    ##Ler frame a frame e aplicar mascara e salvar
    while(True):
        
        #ler frame
        ret, frame = video.read()
        if not ret:
            break
        
        #cortar na regiçao do sensor
        frame = frame[0:1080,0:650]

        #aplicar mascara
        masked = cv2.bitwise_and(mask, frame)
        gray_image = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY) #talvez mudar pra cima
        thresh, binaryFrame = cv2.threshold(gray_image, 220, 255, cv2.THRESH_BINARY )

        #descomentar para salvar frames. fps=30
        #cv2.imwrite('./frames/T-'+str(i)+'.jpg',binaryFrame)
        
        #atualizar tabelas
        ones = np.count_nonzero(binaryFrame)
        df.loc[i] = [str(total)] + [ones] + [total - ones]
        if i == 1461:
            break
        i+=1
        

    #Salvar tabela
    csv_name = file_name.replace("video", "csv")
    csv_name = csv_name.replace(".h264", "")  
    df.to_csv(csv_name)
    video.release()
    cv2.destroyAllWindows()

    #plt.imshow(bw_image2, cmap="gray")
    #plt.show()




