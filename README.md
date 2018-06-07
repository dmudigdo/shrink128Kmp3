# shrink128Kmp3.py

When I need to e-mail songs, I usually shrink them first to 128Kbps MP3s. This way the music is still discernible for music education purposes, but at a smaller file size.

This Python script does just that. Just plonk it in the same folder as the mp3/m4a's you want to shrink, then:

    python shrink128Kmp3.py

## Pydub

This script uses pydub and ffmpeg. To get pydub:

    pip install pydub

To get ffmpeg:

    apt-get install libav-tools libav-tools