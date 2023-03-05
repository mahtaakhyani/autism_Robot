# pip install SpeechRecognition
# https://pypi.python.org/pypi/SpeechRecognition/
# recognizer_instance.recognize_google(audio_data, key = None, language = "fa-IR", show_all = False)
# Performs speech recognition on audio_data (an AudioData instance), using the Google Speech Recognition API.
# The Google Speech Recognition API key is specified by key. If not specified, it uses a generic key that works out of the box.
# This should generally be used for personal or testing purposes only, as it may be revoked by Google at any time.

# NOTE: this example requires PyAudio because it uses the Microphone class
import time
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
r.operation_timeout = 30
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source, timeout=7, phrase_time_limit=5)



# recognize speech using Google Speech Recognition
try:
    print('Trying...')
    transcript = r.recognize_google(audio,language='en-US')
	# for testing purposes, we're just using the default API key
	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	# instead of `r.recognize_google(audio)`
	# print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language = "fa-IR"))
	# print("Google Speech Recognition thinks you said in Turkish: -  " + r.recognize_google(audio, language = "tr-TR"))
    print("Google Speech Recognition thinks you said in persian: -  " + transcript)
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))