

import os
import speech_recognition as sr
import webbrowser


def recognize_speech_from_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now:")
        audio_data = r.listen(source)
    
    try:
        print("Identifying...")
        command = r.recognize_google(audio_data)
        print(f"Command: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError as e:
        print(f"Results not found ; {e}")
        return ""

# Main function
def srp():
    # Recognize speech from microphone input
    command = recognize_speech_from_microphone()
    
    # Perform actions based on recognized command
    if command:
        # Your logic to perform actionable tasks based on the recognized command
        print("Action Performed:", command)

        if 'hey google' in command:
            webbrowser.open("https://google.com/")
            print("Hello how can i assist you")

        elif 'open youtube' in command:
            webbrowser.open("https://youtube.com/")
           

        elif 'open whatsapp'in command:
           webbrowser.open('https://web.whatsapp.com/')
           print("Opening Whatsapp")
        
        else:
            print("Not recognized.")
    else:
        print("Try again.")

# Run the main function
srp()
