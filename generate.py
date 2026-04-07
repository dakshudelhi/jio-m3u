import requests

url = "https://iptv-org.github.io/iptv/countries/in.m3u"

res = requests.get(url)

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(res.text)

print("M3U Generated ✅")
