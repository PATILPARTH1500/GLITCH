import os
import eel 
from playsound import playsound

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\glitchaudio.mp3"
    playsound(music_dir)