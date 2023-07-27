#!/usr/bin/env python
import rospy
from audio_common_msgs.msg import AudioData
import pyaudio
import wave



class AudioCapture:
    pub = rospy.Publisher('captured_audio', AudioData, queue_size=10) #Initiating publisher for publishing captured audio data on the topic /captured_audio
    
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 # 16 bit int sampling
    CHANNELS = 1 # Mono
    RATE = 16000 # Sampling Rate in Hz
    mic = pyaudio.PyAudio()
    
    def __init__(self):
        rospy.init_node('audio_recorder',anonymous=False) 

    
    def capture(self):
        self.stream = self.mic.open(format=self.FORMAT,
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK) 

        data = self.stream.read(self.CHUNK)
        audio_data = AudioData()

        audio_data.data = data
        audio_data.sample_rate = self.RATE
        audio_data.channels = self.CHANNELS
        audio_data.bit_depth = self.mic.get_sample_size(self.FORMAT) * 8

        rospy.loginfo("Capturing Audio data...") #Source: Robot's microphone (not the client's)
        self.pub.publish(audio_data)

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.mic.terminate()




if __name__ == "__main__":
        audcap = AudioCapture()
        rospy.spin()









    
    