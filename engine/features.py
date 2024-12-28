from playsound import playsound
import eel

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\glitchaudio.mp3"
    playsound(music_dir)