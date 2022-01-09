import time
import os
from pymediainfo import MediaInfo
import cv2

####################################################
    #Функции для работы с видео

####################################################
    #Определение длины в секундах
def Duration_Second(filename):
    clip_info = MediaInfo.parse(filename)
    duration_ms = clip_info.tracks[0].duration
    print(str(duration_ms))
    return duration_ms//1000

####################################################
    #Воспроизведение видео
def showVideo(filename):
    # cap = cv2.VideoCapture(filename)
    # ret, frame = cap.read()
    # while True:
    #     ret, frame = cap.read()
    #     if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
    #         cap.release()
    #         cv2.destroyAllWindows()
    #         return
    #     time.sleep(0.02)
    #     cv2.imshow('frame', frame)
    print('Show '+str(filename))
    os.startfile(filename)
