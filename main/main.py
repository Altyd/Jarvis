import os
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_app(app_name):
    # Add more apps here
    app_commands = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "browser": "start chrome",
        "youtube": "start chrome https://www.youtube.com",
        "spotify": "start chrome https://open.spotify.com",
        "github": "start chrome https://github.com/Altyd",
    }
    
    if app_name in app_commands:
        os.system(app_commands[app_name])
    else:
        speak("App not found!")

def main():
    recognizer = sr.Recognizer()
    
    while True:  # Add an infinite loop
        with sr.Microphone() as source:
            print("Listening for 'hey google'...")
            audio = recognizer.listen(source)
            
            try:
                keyword = recognizer.recognize_google(audio).lower()
                if "hey google" in keyword:
                    say = "How can I assist you?"
                    speak(say)
                    print(say)
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio).lower()
                    if "open" in command:
                        app_name = command.split("open ")[1]
                        open_app(app_name)
                    else:
                        idk = "Sorry, I don't understand that command."
                        speak(idk)
                        print(idk)
            except sr.UnknownValueError:
                ohno = "Please say that again"
                #speak(ohno)
                print(ohno)
            except sr.RequestError as e:
                error1 = "Could not request results from Google Speech Recognition service"
                speak(error1)
                print(error1)

if __name__ == "__main__":
    main()
