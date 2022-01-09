import os

import configparser as CP


def createConfig(path):
    """
    Create a config file
    """
    config = CP.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "Если Time_for_processing == 0, то время для обработки определяется автоматически")
    config.set("Settings", "Time_for_processing", "0")

    config.set("Settings", "Capture_Device", "0")
    config.set("Settings", "Capture_Buffer", "120")
    config.set("Settings", "Capture_FPS", "30")
    config.set("Settings", "Capture_Video_Codec_Code", 'MPG4')

    config.set("Settings", "Counter_Limit", '20')

    with open(path, "w") as config_file:
        config.write(config_file)

def readConfig(parametr_name):
    ConfigName = 'Config.txt'
    if not os.path.exists(ConfigName):
        createConfig(ConfigName)
    config = CP.ConfigParser()
    config.read(ConfigName)
    return config.get('Settings',parametr_name)