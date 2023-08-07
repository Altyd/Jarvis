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
    }
    
    if app_name in app_commands:
        os.system(app_commands[app_name])
    else:
        speak("App not found!")

def main():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for 'hello'...")
        audio = recognizer.listen(source)
        
        try:
            keyword = recognizer.recognize_google(audio).lower()
            if "hello" in keyword:
                speak("How can I assist you?")
                print("How can I assist you?")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                if "open" in command:
                    app_name = command.split("open ")[1]
                    open_app(app_name)
                else:
                    speak("Sorry, I don't understand that command.")
                    print("Sorry, I don't understand that command.")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
