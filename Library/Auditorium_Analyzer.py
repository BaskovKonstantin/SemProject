####################################################
    #Класс аудитории
import datetime
import time
import json

class Auditorium (object):
    auditoriumDict = dict()
    auditoriumList = []
    def __init__(self):
        self.auditoriumDict = dict(
            Number_Of_People=0,
            Number_Of_Neutural=0,
            Number_Of_Happy=0,
            Number_Of_Sad=0,
            Number_Of_Suprise=0,
            Number_Of_Anger=0,
            Number_Of_Male=0,
            Number_Of_Female=0,
            Number_Of_Young=0,
            Number_Of_Adult=0,
            Number_Of_Old=0,
        )

    def Zeroing (self):
        self.auditoriumDict = dict(
            Number_Of_People = 0,
            Number_Of_Neutural = 0,
            Number_Of_Happy = 0,
            Number_Of_Sad = 0,
            Number_Of_Suprise = 0,
            Number_Of_Anger = 0,
            Number_Of_Male = 0,
            Number_Of_Female = 0,
            Number_Of_Young = 0,
            Number_Of_Adult = 0,
            Number_Of_Old = 0,
        )

    def Scan (self, Age, Sex, Mood):
        self.auditoriumDict['Number_Of_People']+=1
        HumanDict = dict(
            Sex = None,
            Age = None,
            Mood = None,
            )

        if (Age < 35):
            self.auditoriumDict['Number_Of_Young'] += 1
            HumanDict['Age'] = 'Young'
        if (34 < Age < 60):
            self.auditoriumDict['Number_Of_Adult'] += 1
            HumanDict['Age'] = 'Adult'
        if (Age > 59):
            self.auditoriumDict['Number_Of_Old'] += 1
            HumanDict['Age'] = 'Old'

        if (Sex == 'Male'):
            self.auditoriumDict['Number_Of_Male']+=1
            HumanDict['Sex'] = 'Male'
        if (Sex == 'Female'):
            self.auditoriumDict['Number_Of_Female']+=1
            HumanDict['Sex'] = 'Female'

        if (Mood == 'Neutural'):
            self.auditoriumDict['Number_Of_Neutural'] += 1
            HumanDict['Mood'] = 'Neutural'
        if (Mood == 'Happy'):
            self.auditoriumDict['Number_Of_Happy'] += 1
            HumanDict['Mood'] = 'Happy'
        if (Mood =='Sad'):
            self.auditoriumDict['Number_Of_Sad'] += 1
            HumanDict['Mood'] = 'Sad'
        if (Mood == 'Suprise'):
            self.auditoriumDict['Number_Of_Suprise'] += 1
            HumanDict['Mood'] = 'Suprise'
        if (Mood == 'Anger'):
            self.auditoriumDict['Number_Of_Anger'] += 1
            HumanDict['Mood'] = 'Anger'

        self.auditoriumList.append(HumanDict)

    def get_Number_Of_People(self):
        return self.auditoriumDict['Number_Of_People']


    def Analyse(self):
        Auditorium_Main_Sex, Auditorium_Main_Age, Auditorium_Main_Mood = '', '', ''

        if (self.auditoriumDict['Number_Of_Male'] > self.auditoriumDict['Number_Of_Female']):
            Auditorium_Main_Sex = 'Male'
        else:
            Auditorium_Main_Sex = 'Male'

        Mood_Max = max(self.auditoriumDict['Number_Of_Neutural'],self.auditoriumDict['Number_Of_Happy'],self.auditoriumDict['Number_Of_Sad'],self.auditoriumDict['Number_Of_Suprise'],self.auditoriumDict['Number_Of_Anger'])

        if (Mood_Max == self.auditoriumDict['Number_Of_Neutural']):
            Auditorium_Main_Mood = 'Neutral'
        elif (Mood_Max == self.auditoriumDict['Number_Of_Happy']):
            Auditorium_Main_Mood = 'Happy'
        elif(Mood_Max == self.auditoriumDict['Number_Of_Sad']):
            Auditorium_Main_Mood = 'Sad'
        elif(Mood_Max == self.auditoriumDict['Number_Of_Suprise']):
            Auditorium_Main_Mood = 'Suprise'
        elif (Mood_Max == self.auditoriumDict['Number_Of_Anger']):
            Auditorium_Main_Mood = 'Anger'

        AgeMax = max(self.auditoriumDict['Number_Of_Young'],self.auditoriumDict['Number_Of_Adult'],self.auditoriumDict['Number_Of_Old'])

        if (Mood_Max == self.auditoriumDict['Number_Of_Young']):
            Auditorium_Main_Age = 'Young'
        elif (Mood_Max == self.auditoriumDict['Number_Of_Adult']):
            Auditorium_Main_Age = 'Adult'
        elif(Mood_Max == self.auditoriumDict['Number_Of_Old']):
            Auditorium_Main_Age = 'Old'

        return Auditorium_Main_Sex, Auditorium_Main_Age, Auditorium_Main_Mood

    def formJSON(self):
        data = dict(
            Number_of_People=self.auditoriumDict['Number_Of_People'],
            time = str(datetime.datetime.now()),
            People_Array= self.auditoriumList,
            )
        with open("data_file.json", "w") as write_file:
            json.dump(data, write_file)
