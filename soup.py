from bs4 import BeautifulSoup
import requests

page = requests.get(
    "https://en.wikipedia.org/wiki/List_of_Gilmore_Girls_episodes")
soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.find_all('table', attrs={'class': 'wikiepisodetable'})

data = []
season_episodes = []

for table in tables:
   table_body = table.find('tbody')
   rows = table_body.find_all('tr')
   for row in rows:
      cols = row.find_all('td')
      cols = [element.text.strip() for element in cols]
      data.append([element for element in cols if element])

   for episode in data:
      if len(episode) > 2:
            season_episodes.append(episode[1])

print(season_episodes)
