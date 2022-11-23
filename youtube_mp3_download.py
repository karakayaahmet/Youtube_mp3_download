from pytube import YouTube
import os
from moviepy.editor import *

link = input("Url adresi giriniz: ")

yt = YouTube(link)

print("Ad: ", yt.title)
print("Görüntüleme: ", yt.views)
print("Süre: ", yt.length)

ys = yt.streams.get_audio_only("mp4")

print("İndiriliyor..")

path = ys.download()

mp3_path = os.path.splitext(path)

mp3_path = mp3_path[0] + ".mp3"

os.rename(path, mp3_path)

print("İndirme İşlemi Tamamlandı.")