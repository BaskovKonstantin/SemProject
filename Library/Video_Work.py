from pymediainfo import MediaInfo
import json
import os
import urllib.request
import subprocess
from Library import Config

#####################################################
#Воспроизведение видео



def play_video(video_path):
    print('Show ' + str(video_path))
    vlc_patсh = str(Config.readConfig('VLC_patch'))
    subprocess.Popen([vlc_patсh, video_path])

def play_online_video(url):
    print('Show ' + str(url))
    vlc_patсh = str(Config.readConfig('VLC_patch'))
    print(vlc_patсh)
    subprocess.Popen([vlc_patсh, url])

####################################################
#Определение длины в секундах
def Duration_Second(filename):
    try:
        clip_info = MediaInfo.parse(filename)
        duration_ms = clip_info.tracks[0].duration
        print(str(duration_ms))
    except:
        print('ОШИБКА ПРИ ЧТЕНИИ ФАЙЛА')
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
    with open("answer.json", "r") as read_file:
        data = json.load(read_file)

    file_path = "resource\Video\\"+str(data[filename][0])+".mp4"
    url = data[filename][1]

    exist = os.path.exists(file_path)
    print(exist)

    Video = ''

    if (exist):
       play_video(file_path)
       Video = file_path
    else:
        play_online_video(url)
        Video = url
        urllib.request.urlretrieve(url, file_path)

    return Video



####################################################
#Список локальных видеофайлов

#def getLocalListVideo():

#    ListVideo = os.listdir('resource\Video')

 #   print('Файлы расположенные локально')
 #   print(ListVideo)

   # return ListVideo

















