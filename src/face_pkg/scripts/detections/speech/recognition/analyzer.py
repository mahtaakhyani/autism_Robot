#!/usr/bin/env python
"""A script to extract the following acousting features from an audio file:
- Pitch (minimum, maximum, and average
- Intensity (minimum, maximum, and average
- Jitter
- Shimmer
- HNR (harmonics-to-noise ratio)
- Estimated speaking rate
and save them to a CSV file for further analysis.
"""

import os
import sys

# imports
import glob2
import openpyxl
import pandas as pd
import parselmouth
from parselmouth.praat import call
from tabulate import tabulate

import clustering
file_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(file_dir)

# iterate over all folders and subfolders
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in glob2.glob("*.wav"):
            r.append(os.path.join(root, name))
            sys.path.append(os.path.join(root, name))
        # loads the data
    return r
# sound_files = glob2.glob("%s/**/*.wav"%file_dir)
sound_files = glob2.glob("*.wav")
# sound_files = glob2.glob("temp.wav")
# sound_files = "temp.wav"
# # gets the correct transcript
def get_transcript(path:str, file_name: str) -> str:
    transcription = ""
    with open(path, "r") as source:
        for line in source:
            if line.lower().split(":")[0] == file_name:
                transcription = line.split(":")[1]
    return transcription


def main(transcript=""):
    first_row = [
        "Emotion",
        "Index",
        "Min F0",
        "Max F0",
        "Mean F0",
        "Min Int",
        "Max Int",
        "Mean Int",
        "Jitter",
        "Shimmer",
        "HNR",
        "Speaking Rate",
    ]
    list_files(file_dir)
    table = []
    i = 0
    for file in sound_files:
        file_name = file.split("/")[-1][:-4]
        input_sound = parselmouth.Sound(file)
        # extracts the duration
        duration = input_sound.get_total_duration()
        # extracts the pitch metrics
        pitch = call(input_sound, "To Pitch", 0.0, 75.0, 600.0)
        minF0 = call(pitch, "Get minimum", 0.0, duration, "Hertz", "Parabolic")
        maxF0 = call(pitch, "Get maximum", 0.0, duration, "Hertz", "Parabolic")
        avgF0 = call(pitch, "Get mean", 0.0, duration, "Hertz")
        # extracts the intensity metrics
        intensity = call(input_sound, "To Intensity", 75.0, 0.0)
        min_intensity = intensity.get_minimum()
        max_intensity = intensity.get_maximum()
        avg_intensity = intensity.get_average()
        # extracts jitter
        point_process = call(input_sound, "To PointProcess (periodic, cc)", 75.0, 600.0)
        jitter = call(point_process, "Get jitter (local)", 0.0, 0.0, 0.0001, 0.02, 1.3)
        # extracts shimmer
        shimmer = call(
            [input_sound, point_process],
            "Get shimmer (local)",
            0,
            0,
            0.0001,
            0.02,
            1.3,
            1.6,
        )
        # extracts HNR
        harmonicity = call(input_sound, "To Harmonicity (cc)", 0.01, 75.0, 0.1, 1.0)
        hnr = call(harmonicity, "Get mean", 0, 0)
        # extracts speaking rate
        transcript = get_transcript("transcript.txt", file_name)
        num_words = len(transcript.split())
        speaking_rate = num_words / duration
        print(file.split("/")[-1][:-4])
        # assembles the table
        metrics = [
            file_name,
            i,
            round(minF0, 3),
            round(maxF0, 3),
            round(avgF0, 3),
            round(min_intensity, 3),
            round(max_intensity, 3),
            round(avg_intensity, 3),
            round(jitter, 3),
            round(shimmer, 3),
            round(hnr, 3),
            round(speaking_rate, 3),
        ]
        table.append(metrics)
        i+=1

    df = pd.DataFrame(table, columns=["Emotion",
                                        "Index",
                                        "Min F0",
                                        "Max F0",
                                        "Mean F0",
                                        "Min Int",
                                        "Max Int",
                                        "Mean Int",
                                        "Jitter",
                                        "Shimmer",
                                        "HNR",
                                        "Speaking Rate"])
    df.to_excel('Book1.xlsx', sheet_name='speech_emotion_analyzer', index=False)
    # prints the results
    print(tabulate(table, headers=first_row),'\n')
    # clsf = clustering.Classification()
    # opt = clustering.Optimizer()
    # n = opt.knn_opt()
    # clsf.classify(algorithm='knn' ,n=n)
    # print(clsf.prediction())

if __name__ == "__main__":
    main()
    
