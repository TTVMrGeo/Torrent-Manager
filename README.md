# Setup

Clone repo:

```git clone https://github.com/TTVMrGeo/Torrent-Manager.git```

Install requirements:

you need mpv and [webtorrent-mpv-hook](https://github.com/mrxdst/webtorrent-mpv-hook)
for webtorrent-mpv-hook, setup a config file and set your cache directory, set this in the app settings too

```
# If on windows or mac:

cd Torrent-Manager
pip install flet

# If on linux:

cd Torrent-Manager
python3 -m venv env
source env/bin/activate
pip install flet
```

Running the app:

```
# WHILE IN THE PROGRAM FOLDER

# Windows:
python app.py

# Linux:
source env/bin/activate
python app.py
```
