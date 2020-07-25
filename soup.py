from bs4 import BeautifulSoup
import requests


class Soup:
   def __init__(self):
      """Scrape Wikipedia for Gilmore Girls episode titles,
      Store them in a list
      """
      self.season_episodes = []

      page = requests.get(
         "https://en.wikipedia.org/wiki/List_of_Gilmore_Girls_episodes")
      soup = BeautifulSoup(page.content, 'html.parser')

      tables = soup.find_all('table', attrs={'class': 'wikiepisodetable'})

      data = []

      for table in tables:
         table_body = table.find('tbody')
         rows = table_body.find_all('tr')
         for row in rows:
            cols = row.find_all('td')
            cols = [element.text.strip() for element in cols]
            data.append([element for element in cols if element])

         for episode in data:
            if len(episode) > 2:
                  self.season_episodes.append(episode[1])

   def get_episodes(self):
      return self.season_episodes
