import requests
from lxml import html


def scrape_album_names(artist) -> list:
    for char in ['\'', '(', ')', ' ', '.']:
        artist = artist.replace(char, '' if char != ' ' else '-')
    albums = []
    url = f'https://genius.com/artists/{artist}/albums'
    response = requests.get(url)
    html_content = response.content
    tree = html.fromstring(html_content)
    xpath_query = "//ul/li/a/div[contains(@class, 'ListItem__InfoContainer-sc-122yj9e-3 jGMTGz')]/h3"
    elements = tree.xpath(xpath_query)

    for element in elements:
       albums.append(element.text)

    return albums

def scrape_song_names(artist, album) -> list:
    songs = []
    for char in ['\'', '(', ')', ' ', '.']:
        album = album.replace(char, '' if char != ' ' else '-')
        artist = artist.replace(char, '' if char != ' ' else '-')
    url = f'https://genius.com/albums/{artist}/{album}'
    response = requests.get(url)
    html_content = response.content
    tree = html.fromstring(html_content)
    xpath_query = "//div[contains(@class, 'chart_row-content')]//a[contains(@class, 'u-display_block')]//h3[contains(@class, 'chart_row-content-title')]"
    elements = tree.xpath(xpath_query)

    for element in elements:
        songs.append(element.text)
    songs = [song.strip().replace('\xa0', ' ') for song in songs]

    return songs

if __name__ == '__main__':
    names = scrape_song_names('eminem', 'The Marshall Mathers LP 2 (Expanded Edition)')
    for name in names:
        print(name)


