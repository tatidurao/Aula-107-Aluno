import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

#carregando rastreador na variavel tracker

#lendo primeiro quadro

while True:

    check, img = video.read()
    
    cv2.imshow("resultado", img)


    # Saia da janela de exibição quando a barra de espaço for pressionada
    key = cv2.waitKey(25)
    if key == 32:
        print("Interrompido")
        break

video.release()
cv2.destroyALLwindows()
















