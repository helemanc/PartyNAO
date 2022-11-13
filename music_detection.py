# Import utilities
import pydub 
import glob, os 
import random
import scipy.io.wavfile
import numpy as np 
import matplotlib.pyplot as plt 
from pydub.playback import play 
from threading import Thread
from playsound import playsound

#--------------------------------------------------------------#
# Plot the amplitudes without breaking the execution of the program
class ThreadPlot(Thread):
    def __init__(self, time, audData):
        Thread.__init__(self)
        self.time = time
        self.audData = audData

    def run(self):
        plt.figure("Amplitudes")
        plt.plot(self.time, self.audData, linewidth=0.01, alpha=0.7, color='#ff7f00')
        plt.xlabel('Time(s)')
        plt.ylabel('Amplitude')
        plt.rcParams['agg.path.chunksize'] = 10000
        plt.show()
        

#--------------------------------------------------------------#
# Choose a random song from the folder "Music" contained in the main folder of the project

def random_song():  # hp: exists a folder named 'Music' in which we search songs
    list_songs = []
    os.chdir(os.getcwd() + "/Music")
    for file in glob.glob("*.wav"):
        list_songs.append(file)
    sorted_song = random.choice(list_songs)
    print("I chose the song || " + sorted_song + " || LET' S DANCE NAO!")
    return sorted_song

# Analyze the selected song and plot the amplitudes in order to show how the intensity change into the song.
# The function returns the list of intensity per second of the song


def analyze_music(song):
    wav = pydub.AudioSegment.from_wav(os.getcwd() + "/" + song)
    wav_mono = wav.set_channels(1)
    os.chdir(os.getcwd() + "/Music_Mono")
    wav_mono.export(os.getcwd() + "/" + "_MONO_" + song[:-3] + "wav", format="wav")
    rate, audData = scipy.io.wavfile.read(os.getcwd() + "/" + "_MONO_" + song[:-3] + "wav")

    #####PLOT AMPLITUDE#####
    # create a time variable in seconds
    
    time = np.arange(0, float(audData.shape[0]), 1)/rate
    # plot amplitude over time
    #thread = ThreadPlot(time, audData)
    #print("Now I plot the amplitudes...")
    #thread.start()
    #######################

    # INTENSITY ANALYSIS
    list_interval_intensity = []
    for i in range(180):
        list_interval_intensity.append((np.sum(abs(audData[i*rate:((i+1)*rate)+1]).astype(float)))/rate)
    max_interval = max(list_interval_intensity)
    list_interval_intensity_percent = []

    for el in list_interval_intensity:
        list_interval_intensity_percent.append((el*100)/max_interval)
    return list_interval_intensity_percent


# Play the selected song
def play_song(song):
    os.chdir('..')
    playsound(os.getcwd() + "/" + song)
    #wav = pydub.AudioSegment.from_wav(os.getcwd() + "/" + song)
    #play(wav)
