import speech_recognition as sr
import wikipedia 

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    rr=("You said: " + r.recognize_google(audio))
    print(rr)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

#if wikipedia in rr:
	#speak('Searching wikipedia....')
	#rr=rr.replace("wikipedia","")
	#results = wikipedia.summary(rr,sentences=2)
	#speak('According to wikipedia')
	#print(results)
	#speak(results)

	
	
	
