import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def speak_text(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Loop infinitely for user to speak
while True:
    try:
        # Use the microphone as source for input
        with sr.Microphone() as source:
            # Wait for a second to let the recognizer adjust the energy threshold
            r.adjust_for_ambient_noise(source, duration=0.2)
            
            # Listen for the user's input
            print("Listening...")
            audio = r.listen(source)
            
            # Use Google to recognize audio
            text = r.recognize_google(audio)
            text = text.lower()
            
            print(f"Did you say: {text}")
            speak_text(text)
    
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    
    except sr.UnknownValueError:
        print("Unknown error occurred")

    except KeyboardInterrupt:
        print("Program terminated by user")
        break
