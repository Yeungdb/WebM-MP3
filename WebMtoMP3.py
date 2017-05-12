#!/usr/bin/python

from glob import glob
from optparse import OptionParser
import subprocess 

parser = OptionParser()
parser.add_option('-f', "--filename", help="Filename", action="store")

options, args = parser.parse_args()

fileList = glob('{FILENAME}'.format(FILENAME=options.filename))

for SongName in fileList:
    SongName = SongName.split('./')[1].split('.webm')[0]
    subprocess.call("ffmpeg -i \"{SongName}.webm\" -acodec libmp3lame -aq 4 \"{SongName}.mp3\"".format(SongName = SongName), shell=True)
