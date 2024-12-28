import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        
        audio = r.listen(source, 10 , 6)
        
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")
    except Exception as e:
        return ""
    
    return query.lower()

    
text = takecommand()
speak(text)