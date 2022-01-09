import cv2
import numpy as np
from cv2.cv2 import CAP_PROP_BUFFERSIZE, CAP_PROP_FOURCC, CAP_PROP_FPS, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH, \
    INTER_AREA
from openvino.inference_engine import IECore

####################################################
    #Файлик с функциями детекции

def Age_Gender_Detect(img):

    ie = IECore()
    Age_Gender_net_Patch='resource\OpenVINO Models\\age-gender-recognition-retail-0013\\FP16\\age-gender-recognition-retail-0013.xml'

    Age_Gender_net = ie.read_network(Age_Gender_net_Patch)
    print(Age_Gender_net.input_info.keys())
    print(Age_Gender_net.outputs)

    Age_Gender_net_input_blob = next(iter(Age_Gender_net.input_info))
    Age_Gender_net_output_blob = next(iter(Age_Gender_net.outputs))

    device="CPU"
    exec_net = ie.load_network(network=Age_Gender_net, device_name=device)

    _, _, net_h, net_w = Age_Gender_net.input_info[Age_Gender_net_input_blob].input_data.shape
    print(str(net_w) + ' ' + str(net_h))


    MaleCounter = 0
    FemaleCounter = 0
    AgeAverage = 0

    Iteration = 1
    counter = 0


    img = cv2.resize(img, (net_w, net_h), INTER_AREA)
    print('Resize Face')

    img = np.expand_dims(img, axis=0)
    print('Expand Face')
    img = img.transpose((0, 3, 1, 2))
    print('Transpose Face')

    res = exec_net.infer(
        inputs={Age_Gender_net_input_blob: img}
    )
    print(str(res['age_conv3']))
    age = round(100*res['age_conv3'][0][0][0][0])
    print('Предположительный возраст: '+ str(age))
    AgeAverage += age


    Female = res['prob'][0][0][0][0]
    Male = res['prob'][0][1][0][0]
    print('Male:'+ str(Male))
    print('Female:' + str(Female))

    Sex = (Female+Male)/2

    print('Sex: '+ str(Sex))


    if (Male>Female):
        FinalSex = 'M'
        print('FINAL SEX: MALE')
    else:
        FinalSex = 'F'
        print('FINAL SEX: FEMALE')
    AgeAverage=AgeAverage
    print('FINAL AGE:' + str(AgeAverage))

    return AgeAverage,FinalSex

def Mood_Detect(img):


    Mood_net_Patch='resource\OpenVINO Models\emotions-recognition-retail-0003\\FP16\emotions-recognition-retail-0003.xml'
    ie = IECore()
    Mood_net = ie.read_network(Mood_net_Patch)
    print(Mood_net.input_info.keys())
    print(Mood_net.outputs)

    Mood_net_input_blob = next(iter(Mood_net.input_info))
    Mood_net_output_blob = next(iter(Mood_net.outputs))

    device="CPU"
    exec_net = ie.load_network(network=Mood_net, device_name=device)

    _, _, net_h, net_w = Mood_net.input_info[Mood_net_input_blob].input_data.shape
    print(str(net_w) + ' ' + str(net_h))


    img = cv2.resize(img, (net_w, net_h), INTER_AREA)
    print('Resize Face')

    img = np.expand_dims(img, axis=0)
    print('Expand Face')
    img = img.transpose((0, 3, 1, 2))
    print('Transpose Face')

    res = exec_net.infer(
        inputs={Mood_net_input_blob: img}
    )


    Neutral = res['prob_emotion'][0][0][0][0]
    Happy = res['prob_emotion'][0][1][0][0]
    Sad = res['prob_emotion'][0][2][0][0]
    Suprise = res['prob_emotion'][0][3][0][0]
    Anger = res['prob_emotion'][0][4][0][0]

    Max = max(Neutral,Happy,Sad,Suprise,Anger)

    if (Max == Neutral):
        return 'Neutral', (120,120,120)
    if (Max == Happy):
        return 'Happy', (0,255,0)
    if (Max == Sad):
        return 'Sad', (160,0,20)
    if (Max == Suprise):
        return 'Suprise', (255,255,0)
    if (Max == Anger):
        return 'Anger',(0,0,255)

def Face_Detect(img):
    ie = IECore()
    device = "CPU"

    Face_Detection_net_Path = 'resource\OpenVINO Models\\face-detection-0206\\FP16\\face-detection-0206.xml'

    Face_Detection_net = ie.read_network(Face_Detection_net_Path)
    print(Face_Detection_net.input_info.keys())
    print(Face_Detection_net.outputs)

    Face_Detection_net_input_blob = next(iter(Face_Detection_net.input_info))
    Face_Detection_net_output_blob = next(iter(Face_Detection_net.outputs))

    _, _, Face_Detection_net_height, Face_Detection_net_width = Face_Detection_net.input_info[
        Face_Detection_net_input_blob].input_data.shape

    exec_Face_Detection_net = ie.load_network(network=Face_Detection_net, device_name=device)

    height, width, _ = img.shape

    img = cv2.resize(img, (Face_Detection_net_width, Face_Detection_net_height),
                     INTER_AREA)  # Подгока изображения под детекцию лиц
    print('Resize Frame')
    img = img.transpose((2, 0, 1))
    print('Transpose Frame')

    res = exec_Face_Detection_net.infer(
        inputs={Face_Detection_net_input_blob: img}
    )

    box_coord = res['boxes']
    labels_coord = res['labels']

    width_sc, height_sc = width / Face_Detection_net_width, height / Face_Detection_net_height

    return box_coord,labels_coord,width_sc,height_sc