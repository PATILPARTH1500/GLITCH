import pyttsx3
import speech_recognition as sr
import eel


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 160)
    print(voices)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening....') 
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        # Adjusting timeout and phrase_time_limit
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
        
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I did not catch that.")
        return ""

    return query.lower()


