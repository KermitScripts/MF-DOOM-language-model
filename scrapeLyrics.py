import requests
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = "https://www.songlyrics.com/mf-doom-lyrics/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

req = Request(url, headers=headers)
page = urlopen(req)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

table_element = soup.find('table', class_='tracklist')

tr_elements = table_element.find('tbody').find_all('tr')

links = []
for tr in tr_elements:
    a_element = tr.find('a')
    if a_element:
        link = a_element['href']
        links.append(link)

lyrics_list = []

with open("lyrics.txt", "w", encoding="utf-8") as file:
    for link in links:
        response = requests.get(link)
        if response.status_code == 200:
            page_content = response.text
            soup = BeautifulSoup(page_content, 'html.parser')

            lyrics_element = soup.find('p', id='songLyricsDiv', class_='songLyricsV14')

            if lyrics_element:
                lyrics_text = lyrics_element.get_text()
                file.write(f"\n\n{lyrics_text}\n")

print("Lyrics saved to lyrics.txt")


