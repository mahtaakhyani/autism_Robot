import numpy as np
from praatio import textgrid as tgio
import parselmouth as pm

# Define the parameters of the vowel sound
duration = 0.3
f0 = 150.0
formants = [(500, 2000, 3200), (2800, 3500, 4480)]

# Create a PRAAT TextGrid object to hold the sound

tg = tgio.Textgrid()
# tg.addTier(tgio.IntervalTier("vowel", [(0.0, duration)]))
# define a constructor for the TextGrid object
tg = tgio.Textgrid(["vowel"])
# define a constructor for the IntervalTier object 
tg.tierDict["vowel"] = tgio.IntervalTier("vowel", [(0.0, duration, "vowel")])

# Create a PRAAT Pitch object to hold the pitch contour
pitch = pm.Pitch(f0, 75, 500, 0.01, 0.45, 0.01, 0.35, "Hertz")
# synthesizes speech from text with parselmouth
app = pm.PraatApp()
synthVowel = app.openScript("synth_vowel.praat")
# Create a PRAAT Formant object to hold the formant frequencies
formant = pm.Formant(*formants)

# Generate the synthetic sound using PRAAT's synthesis functions
wave = synthVowel(pitch, formant, None, duration, "hanning")

# Save the resulting waveform as a WAV file
app.writeWaveFile("synth_vowel.wav", np.array(wave), 44100, 16)