####################################################
    #Файлик для Испытаний



from pymediainfo import MediaInfo
clip_info = MediaInfo.parse('../resource/Video/Female.mp4')
duration_ms = clip_info.tracks[0].duration
print(str(duration_ms))