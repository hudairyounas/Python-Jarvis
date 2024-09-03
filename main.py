# import speech_recognition as sr
# # import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()


# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:
#         # Listen for the wake word "Jarvis"
#         # obtain audio from the microphone
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Listening...")
#             audio = r.listen(source, timeout=2)

#         print("recognizing...")
#         recognizer.adjust_for_ambient_noise(source)
#         try:
#             commend = r.recognize_sphinx(audio)
#             print(commend)
#         except Exception as e:
#             print("Error; {0}".format(e))



# import speech_recognition as sr
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:

#             print("Recognizing...")
#             try:
#                 with sr.Microphone() as source:
#                     print("Listening...")
#                 recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#                 audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)  # Increased timeout
#                 command = recognizer.recognize_google(audio)
#                 print("You said: " + command)
#             except Exception as e:
#                 print("Could not request results from Google Speech Recognition service; {0}".format(e))
                

# Could not request results from Google Speech Recognition service; Audio source must be entered before adjusting, see documentation for ``AudioSource``; are you using ``source`` outside of a ``with`` statement?

# import speech_recognition as sr
# import pyttsx3

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()


# def processCommand(commend):
#     print(commend)

# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#                 audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)  # Listen for the audio

#             print("Recognizing...")
#             word = recognizer.recognize_google(audio)
#             if word.lower() == "jarvis":
#                 speak("Ya")
#                 with sr.Microphone() as source:
#                     print("Listening...")
#                 recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#                 audio = recognizer.listen(source)
#                 command = recognizer.recognize_google(audio)

#                 processCommand(command) 

#         except Exception as e:
#             print("An error occurred: {0}".format(e))


# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engin = pyttsx3.init()


# def speak(text):
#     engin.say(text)
#     engin.runAndWait()

# def processCommend(c):
#     print(c)

# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:
#         r = sr.Recognizer()

#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if(word.lower() == "jarvis"):
#                 speak("Ya")
#                 with sr.Microphone() as source:
#                     print("Jarvis Active...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)

#                     processCommend(command)

#         except Exception as e:
#             print("Error; {0}".format(e))


# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# recognizer = sr.Recognizer()
# engin = pyttsx3.init()

# def speak(text):
#     engin.say(text)
#     engin.runAndWait()

# def processCommend(c):
#     print(c)

# if __name__ == "__main__":
#     speak("Initializing Jarvis....")
#     while True:
#         r = sr.Recognizer()
#         print("recognizing...")
#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#             word = r.recognize_google(audio)
#             if word.lower() == "jarvis":
#                 speak("Ya")
#                 with sr.Microphone() as source:
#                     print("Jarvis Active...")
#                     audio = r.listen(source)
#                     command = r.recognize_google(audio)
#                     processCommend(command)
#         except Exception as e:
#             print("Error; {0}".format(e))


import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engin = pyttsx3.init()
newsapi = "8bbd2fef1aee464bb8092de27367b4d1"

def speak(text):
    engin.say(text)
    engin.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        pass



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio).lower()
                if word == "jarvis":
                    speak("Ya")
                    print("Jarvis Active...")
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=1, phrase_time_limit=2)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")