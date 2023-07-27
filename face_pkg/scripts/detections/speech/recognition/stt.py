# pip install SpeechRecognition
# https://pypi.python.org/pypi/SpeechRecognition/
# recognizer_instance.recognize_google(audio_data, key = None, language = "fa-IR", show_all = False)
# Performs speech recognition on audio_data (an AudioData instance), using the Google Speech Recognition API.
# The Google Speech Recognition API key is specified by key. If not specified, it uses a generic key that works out of the box.
# This should generally be used for personal or testing purposes only, as it may be revoked by Google at any time.

# NOTE: this example requires PyAudio because it uses the Microphone class
import time
import pyaudio, wave
import analyzer
import speech_recognition as sr

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
timeout = 7

# obtain audio from the microphone
r = sr.Recognizer()
r.operation_timeout = 30
with sr.Microphone() as source:
	print("Say something!")
	print('Recording...')

	frames = []  # Initialize array to store frames
	audio = r.listen(source, timeout=timeout, phrase_time_limit=5)


	frames.append(audio.get_raw_data())
	wf = wave.open('happy.wav', 'wb')
	wf.setnchannels(channels)
	wf.setsampwidth(audio.sample_width)
	wf.setframerate(fs)
	wf.writeframes(b''.join(frames))
	wf.close()



# recognize speech using Google Speech Recognition
try:
	print('Trying...')
	# transcript = r.recognize_google(audio,language='fa-IR')
	transcript = "خدا همین یعنی همه جا دارم اینا رو میزارن همه چی"
	# for testing purposes, we're just using the default API key
	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	# instead of `r.recognize_google(audio)`

	print("Google Speech Recognition thinks you said in persian: -  " + transcript)
	with open("transcript.txt","w+", encoding="utf-8") as tr:
		tr.write(transcript)
		tr.close()
	analyzer.main(transcript)
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))