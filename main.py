import os
from moviepy.editor import *

directory = os.fsencode('mp4')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".mp4"):
        video = VideoFileClip(os.path.join("mp4/" + filename))
        video.audio.write_audiofile(os.path.join("mp3/" + filename + ".mp3"))
        continue
    else:
        continue
