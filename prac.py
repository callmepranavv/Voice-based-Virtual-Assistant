import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
	print('Speak....')
	audio = r.listen(source)

	try:
		text = r.recognizer_google(audio)
		print('you said : {}'.format(text))
	except:
		print('sorry')