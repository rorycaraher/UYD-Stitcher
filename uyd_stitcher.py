import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.stitcher.com/podcast/uhh-yeah-dude")

soup = BeautifulSoup(r.text, 'html.parser')

latest_episode = soup.find('section', {'id': 'currentEpisode'})
episode_onclick = latest_episode.findChildren('a')[0]['onclick']
onclick_split = episode_onclick.split(',')[2]
episode_id = onclick_split.split('_')[1].replace("'","")
latest_episode_link = "https://www.stitcher.com/podcast/uhh-yeah-dude/e/" + episode_id

print(latest_episode_link)
