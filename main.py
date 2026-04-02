from pathlib import Path
from urllib.parse import urlparse, parse_qs
import json, re, subprocess

class torrent_management():
    def __init__(self, path, c_path):
        self.saved_path = path
        self.cache_path = c_path

    def load(self, path):
        return json.load(open(path, "r"))

    def write(self, data, path):
        json.dump(data, open(path, "w"), indent=4)

    def name(self, link):
        flags = ["1080p", "REPACK", "NF", "WEB-DL", "DUAL", "AAC2.0", "H.264", "ABMA", "DDP2.0", "H", "264-VARYG", "AMZN", "HVEC", "10-bit", "HDR", "Dolby Vision", "Remux", "FLAC", "Opus", "AAC", "E-AC3", "TrueHD", "DTS", "BluRay", "WEB-DL", "DVD", "MULTI", "DUBBED"]
        for item in re.split(r"\[[^\]]*\]", parse_qs(urlparse(link).query)['dn'][0]):
            if item != '':
                for name in re.split(r"\([^)]*\)", item.strip()):
                    if name != '':
                        for flag in flags:
                            name = name.replace(flag, "")
                        return name.strip()
                
    def save(self, link):
        saved = self.load(self.saved_path)
        saved[self.name(link)] = link
        self.write(saved, self.saved_path)

    def remove(self, item):
        saved = self.load(self.saved_path)
        saved.pop(item)
        self.write(saved, self.saved_path)

    def play(self, item):
        link = self.load(self.saved_path)[item]
        subprocess.run(["mpv", link])
        subprocess.getoutput(f"rm -rf {self.cache_path}/*")