#!/usr/bin/env python3
"""Bulk-download audio from Instagram Reels. Thin wrapper over yt-dlp (needs ffmpeg)."""
import argparse
import sys

from yt_dlp import YoutubeDL


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("urls", nargs="*", help="reel URLs")
    p.add_argument("-f", "--file", help="text file with one URL per line (# comments ok)")
    p.add_argument("-o", "--out", default="downloads", help="output dir (default: downloads)")
    p.add_argument("--format", default="mp3", help="audio format: mp3, m4a, opus, wav (default: mp3)")
    p.add_argument("--cookies-from-browser", metavar="BROWSER",
                   help="chrome, firefox, edge... (Instagram often requires login)")
    a = p.parse_args()

    urls = list(a.urls)
    if a.file:
        with open(a.file, encoding="utf-8") as fh:
            urls += [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    if not urls:
        p.error("give URLs or --file")

    opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{a.out}/%(uploader)s - %(id)s.%(ext)s",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": a.format}],
        "ignoreerrors": True,  # skip failed reels, keep going
        "download_archive": f"{a.out}/.archive.txt",  # re-runs skip finished reels
    }
    if a.cookies_from_browser:
        opts["cookiesfrombrowser"] = (a.cookies_from_browser,)

    with YoutubeDL(opts) as ydl:
        failed = ydl.download(urls)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
