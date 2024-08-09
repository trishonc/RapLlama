import requests
from bs4 import BeautifulSoup

url = 'https://genius.com/Lil-baby-humble-lyrics'

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')

divs = soup.select('div.Lyrics__Container-sc-1ynbvzw-1.kUgSbL')

lyrics = []

for div in divs:
    lyrics.append(div.get_text(separator="\n", strip=True))

print(str(lyrics))
