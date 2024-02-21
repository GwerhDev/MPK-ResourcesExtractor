# MKP Resources Extractor

An MPK resource extractor is a tool used to unpack or extract resources from MPK files, often associated with certain software or games, contain various types of resources such as images, audio files, videos, and more. Extractors like this one allow users to access and manipulate these resources for various purposes, such as modding, debugging, or analyzing the contents of the files.

This project is based on this [repository](https://github.com/mindphluxnet/MPKExtractor) by [mindphluxnet](https://github.com/mindphluxnet)

## Use

Requires Python 3.8.x

This software extracts the .mpkinfo files and saves them in the "MPK Resources Extractor" directory, which opens upon completion.

You can run it directly from your IDE or build it using the console with:

```bash
pyinstaller --onefile --noconsole --icon=src/assets/logo.ico --add-data "src;src" main.py
```

## Dist

You can download this software for Windows [here](https://developers-terminalkiller.fly.dev/gwerh/download/mkpre-installer.exe)