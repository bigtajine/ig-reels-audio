# ig-reels-audio

Bulk-download the audio from Instagram Reels. Wraps [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Setup

```
pip install -r requirements.txt
```
Also install [ffmpeg](https://ffmpeg.org/) and put it on PATH (`winget install ffmpeg`).

## Use

```
python reels_audio.py https://www.instagram.com/reel/XXXX/ https://www.instagram.com/reel/YYYY/
python reels_audio.py -f urls.txt --format m4a -o music
python reels_audio.py -f urls.txt --cookies-from-browser chrome   # if Instagram demands login
```

`urls.txt`: one URL per line, `#` lines ignored. Finished reels are recorded in `<out>/.archive.txt`, so re-running skips them.

Only download content you have the right to use.
