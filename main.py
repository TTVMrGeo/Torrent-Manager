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
        return(re.split(r"\[[^\]]*\]", parse_qs(urlparse(link).query)['dn'][0])[1].strip())

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