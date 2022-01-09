import time

import cv2
from Library import Detection
from Library import Config
from Library import Auditorium_Analyzer
from cv2.cv2 import CAP_PROP_BUFFERSIZE, CAP_PROP_FPS, CAP_PROP_FOURCC
####################################################
    #Файл в котором производиться запись видео и его первичный анализ

def VideoCapture_and_Analyse():

    Capture_Device = int(Config.readConfig('Capture_Device'))
    Capture_Buffer = int(Config.readConfig('Capture_Buffer'))
    Capture_FPS = int(Config.readConfig('Capture_FPS'))
    Capture_Video_Codec_Code = Config.readConfig('Capture_Video_Codec_Code')


    cap = cv2.VideoCapture(Capture_Device)
    cap.set(CAP_PROP_BUFFERSIZE, Capture_Buffer)
    cap.set(CAP_PROP_FPS, Capture_FPS)

    fourcc_cap = cv2.VideoWriter_fourcc(*Capture_Video_Codec_Code)
    cap.set(CAP_PROP_FOURCC, fourcc_cap)

    #######################################################################################################

    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # Ширина кадров в видеопотоке.
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Высота кадров в видеопотоке.

    # ret, img = cap.read()
    # h, w, _ = img.shape

    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('otg.mp4', fourcc, 20.0, (w, h))

    #######################################################################################################

    counter = 0
    Timer = time.time()
    Сounter_Limit = int(Config.readConfig("Counter_Limit"))
    Auditorum = Auditorium_Analyzer.Auditorium()

    #######################################################################################################

    while cap.isOpened():
        Auditorum.Zeroing() # Добавил для того, чтобы сделать запись, с этой строчкой все данные будут определятся по последему кадру

        ret, img = cap.read()
        print('Take a Frame')
        orig_img = img

        #######################################################################################################

        if (counter % 20 == 0 or counter == 0):

            try:

                box_coord, labels_coord, width_scale, height_scale = Detection.Face_Detect(img)

            except cv2.error:
                try:

                    print('Show Frame without painting')
                    cv2.imshow('Trry', orig_img)
                    # out.write(orig_img)

                except cv2.error:
                    continue

                continue

            print('Take result')

        #######################################################################################################

        for i, detection in enumerate(box_coord):

            class_id = labels_coord[i]

            xmin, ymin, xmax, ymax, confidence = detection

            xmin = int(xmin * width_scale)
            xmax = int(xmax * width_scale)
            ymin = int(ymin * height_scale)
            ymax = int(ymax * height_scale)

            if confidence > 0.5:
                Face = orig_img[ymin:ymax, xmin:xmax]
                Age, Sex = Detection.Age_Gender_Detect(Face)
                Mood, Color = Detection.Mood_Detect(Face)

                Auditorum.Scan(Age, Sex, Mood)

                print('Detect Age, Gender and Mood')

                cv2.rectangle(orig_img, (xmin, ymin), (xmax, ymax), Color, 2)
                cv2.putText(orig_img, 'Age:' + str(Age) + ' Sex:' + str(Sex) + ' Mood:' + str(Mood),
                            (xmin + 10, ymin - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, Color)
                print('Paint rect and text')

        #######################################################################################################

        counter = counter + 1
        print(counter)
        try:
            cv2.imshow('Trry', orig_img)
            # out.write(orig_img)
            print('Show Frame')
        except cv2.error:
            continue
        if (cv2.waitKey(10) == 27 or counter == Сounter_Limit):
            # out.imshow()
            cap.release()
            cv2.destroyAllWindows()
            break
    print('Людей обнаруже'+str(Auditorum.get_Number_Of_People()))
    Auditorum.formJSON()
    Timer = time.time() - Timer
    Auditorium_Main_Sex, Auditorium_Main_Age, Auditorium_Main_Mood = Auditorum.Analyse()
    return Auditorium_Main_Sex, Auditorium_Main_Age, Auditorium_Main_Mood, Timer

