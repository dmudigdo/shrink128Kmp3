#
# Scans directory for .m4a file (e.g. from Apple iTunes) or .mp3, outputs
# file as a 128Kbps MP3, for a smaller file size
#

import os
from pydub import AudioSegment

# Get the filenames

tracks = os.listdir('.')

# Loop through the filenames for m4a

for track in tracks:

    # Split filename into name + extension then check if it is a .m4a or mp3

    splitname = os.path.splitext(track) 

    # m4a:
    if splitname[1] == ".m4a":
        print ".m4a file found: " + splitname[0] + splitname[1]

        # Import
    
        song = AudioSegment.from_file(track,"m4a")

        # Export as 128Kbps MP3

        song.export(splitname[0] + ".mp3", format="mp3",  bitrate="128k")

    #endif

    # mp3:
    if splitname[1] == ".mp3":
        print ".mp3 file found: " + splitname[0] + splitname[1]

        # Import
    
        song = AudioSegment.from_file(track,"mp3")

        # Export as 128Kbps MP3

        song.export(splitname[0] + "_128k.mp3", format="mp3",  bitrate="128k")

    #endif
#endfor
