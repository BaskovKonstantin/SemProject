import json
import time
from collections import OrderedDict

from Library import Config
from Library import VideoCapture, Video_Work
import cv2

### Выполнение основной функции
Auditorium_Main_Sex, _, Auditorium_Main_Mood,Time_for_processing = VideoCapture.VideoCapture_and_Analyse()
pos = 0
err = 0

while True:
    print('Choose Video')

    with open("answer.json", "r") as read_file:
        data = json.load(read_file)

    data = data['VideoList']
    filename = data[pos]

    if (err>0):
        pos+=1
        if (pos>=len(data)):
            pos = 0

    try:
        filename =  Video_Work.showVideo(filename)
    except:
        filename = 'Anger'
        filename = Video_Work.showVideo(filename)


    VideoDuration_second = Video_Work.Duration_Second(filename)

    ##Время на обработку можно установить в конфиге, 0 - автоматическое определение
    if (int(Config.readConfig("Time_for_processing"))>0):
        Time_for_processing = int(Config.readConfig("Time_for_processing"))
    else:
        Time_for_processing*=1.5
    WaitingRatio = 1-(int(Time_for_processing)/VideoDuration_second)
    WaitingTime = WaitingRatio*VideoDuration_second

    print('Длительность видео: ' + str(VideoDuration_second)+'c')
    print('Коэфициент Ожидание' + str(WaitingRatio))
    print('Время ожидания: ' + str(WaitingTime) + 'с')

    ####################################################

    print('Wait_1')
    time.sleep(WaitingTime)

    print('Analyze')
    Auditorium_Main_Sex, _, Auditorium_Main_Mood,Time_for_processing = VideoCapture.VideoCapture_and_Analyse()
    if (cv2.waitKey(10) == 27):
        cv2.destroyAllWindows()
        break