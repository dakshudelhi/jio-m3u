import requests

channels_api = "https://jiotvapi.vercel.app/api/channels"

res = requests.get(channels_api)
data = res.json()

m3u = "#EXTM3U\n"

for ch in data:
    name = ch.get("name")
    url = ch.get("url")
    logo = ch.get("logo")

    m3u += f'#EXTINF:-1 tvg-logo="{logo}",{name}\n{url}\n'

with open("playlist.m3u", "w", encoding="utf-8") as f:
    f.write(m3u)

print("M3U Generated ✅")
