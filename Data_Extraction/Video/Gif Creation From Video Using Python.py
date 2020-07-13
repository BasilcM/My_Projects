#pip install moviepy

from moviepy. editor import *

clip = (VideoFileClip("ENTER THE FILE PATH HERE"))
clip. write_gif("output.gif")
