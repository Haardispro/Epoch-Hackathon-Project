from youtube_search import YoutubeSearch
import json
from pytube import YouTube
from pydub import AudioSegment
from os import path
import subprocess
import os


def background_music():
    background_music = str(input("Enter Background Music name:"))
    
    results = YoutubeSearch(background_music, max_results=1).to_json()
    results_dict = json.loads(results)

    for v in results_dict['videos']:
        x = 'https://www.youtube.com' + v['url_suffix']
        bg = YouTube(x)
    video = bg.streams.filter(only_audio=True).first()
    destination = "temp/"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = 'temp/'+ 'sound1' + '.mp3'
    os.rename(out_file, new_file)
    print(video.title + " has been successfully downloaded.")

# Vocals 
def vocals(): 
    vocals = str(input("Enter Vocals Music: "))
    
    results = YoutubeSearch(vocals, max_results=1).to_json()
    results_dict = json.loads(results)

    for v in results_dict['videos']:
        y = 'https://www.youtube.com' + v['url_suffix']
        voc_al = YouTube(y)
    video = voc_al.streams.filter(only_audio=True).first()
    destination = "temp/"
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = 'temp/' + 'sound2' + '.mp3'
    os.rename(out_file, new_file)
    print(video.title + " has been successfully downloaded.")

if input("Download Background Music(Y/N):") == "Y":
    background_music()
else: 
    exit()
if input("Download Vocals(Y/N):") == "Y":
    vocals()
else:
    exit()

if input("Do you want to mix both of the tracks? (Y/N):") == "Y":
    background_music = subprocess.call(['ffmpeg', '-i', 'temp/sound1.mp3',
                   'temp/sound1.wav'])
    vocals = subprocess.call(['ffmpeg', '-i', 'temp/sound2.mp3',
                   'temp/sound2.wav'])

    sound1 = AudioSegment.from_file("temp/sound1.wav")
    sound2 = AudioSegment.from_file("temp/sound2.wav")
    combined = sound1.overlay(sound2)
    combined.export("output.wav", format="wav")

else: 
    exit()

