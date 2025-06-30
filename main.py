# importing necessary libraries
# This code is a simple voice assistant that can respond to specific commands and perform actions like opening websites, telling jokes, playing songs, and providing information about itself. It uses speech recognition to understand user commands and text-to-speech to respond.
# It also includes a basic error handling mechanism for unrecognized commands.
import pyttsx3 
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import os
import smtplib
import time
# Function for converting speech to text

def sptext():
  recognizer =sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening.....")
    recognizer.adjust_for_ambient_noise(source,duration=0.5)
    audio=recognizer.listen(source)
    try:
      print("Recognizing...")
      data=recognizer.recognize_google(audio)
      return data
    except sr.UnknownValueError:
      print("Not Understanding...")
#Function for converting text to speech

def speak(text):
  engine=pyttsx3.init()
  voices=engine.getProperty('voices')
  engine.setProperty('voice',voices[1].id)
  rate=engine.getProperty('rate')
  engine.setProperty('rate',150)
  engine.say(text)
  engine.runAndWait()
  
# Main function to run the voice assistant

if __name__ == '__main__':
 
    data = sptext().lower()
    if "hey alexa" in data:
      print("Activation successful.")
      speak("Hello shiwansh, how can I help you?")
      speak("Please say the magic word to continue.")
      while True:
        data1 = sptext().lower()
        if "your name" in data1:
           name="my name is alexa"
           speak(name)
        elif "old" in data1:
           age="i am 20 years old"
           speak(age)
        elif "doing" in data1:
           task="i am doing great, thank you for asking."
           speak(task)
        elif "time" in data1:
           current_time = datetime.datetime.now().strftime("%I:%M %p")
           speak(f"The current time is {current_time}")

        elif 'youtube' in data1:
           speak("opening youtube for you.")
           webbrowser.open("https://www.youtube.com/")
           time.sleep(4)
        elif 'chat' in data1:
           speak("Opening chatgpt for you.")
           webbrowser.open("https://chatgpt.com/?model=")
           time.sleep(4)
        elif 'flip' in data1:
           speak("opening flipkart for you.")
           webbrowser.open("https://www.flipkart.com/")
           time.sleep(4)
        elif 'link' in data1:
           speak("opening linkedin for you.")
           webbrowser.open("https://www.linkedin.com/feed/")
           time.sleep(4)
        elif "joke" in data1:
           joke_1=pyjokes.get_joke(language="en",category="neutral")
           print(joke_1)
           speak(joke_1)
        elif "song" in data1:
           add=r"C:\Users\shiwa\OneDrive\Desktop\songs"
           listsong=os.listdir(add)
           print("playing song...") 
           os.startfile(os.path.join(add,listsong[2]))
           time.sleep(8)
        elif "exit" in data1:
           speak("Thank you shiwansh for using me, have a nice day!")
           break
        else:
           speak("sorry i don't know the command")
        time.sleep(2)
        
    else:
        speak("You didn't say the magic word.")