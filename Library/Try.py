####################################################
    #Файлик для Испытаний
import json
data = dict(
        VideoList = ['Angry','Happy'],
        Angry = ['Angry','urlAngry'],
        Happy = ['Happy', 'urlHappy']
    )

with open("answer.json", "w") as write_file:
    json.dump(data, write_file)