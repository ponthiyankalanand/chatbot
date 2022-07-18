#!/usr/bin/env python3
# Requires PyAudio and PySpeech. 
import speech_recognition as sr
def speechtotext(): 
# Record Audio
   
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening....")
       
      audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
      try:
# for testing purposes, we're just using the default API key
# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# instead of `r.recognize_google(audio)`
         recaudio = r.recognize_google(audio)
         print("You said: " + recaudio)
      except sr.UnknownValueError:
         print("System could not understand audio") 
         recaudio = "sorry"       
      except sr.RequestError as e:
         print("Could not request results from Google Speech Recognition service; {0}".format(e))
         recaudio = "sorry"
   return(recaudio)