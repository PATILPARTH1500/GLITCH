import os
import eel

# from engine.features import *
eel.init("www")

# playAssistantSound()

os.system('start chrome.exe --app="http://127.0.0.1:3000/engine/www/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)

