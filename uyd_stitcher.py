import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.stitcher.com/podcast/uhh-yeah-dude")

soup = BeautifulSoup(r.text, 'html.parser')

latest_episode = soup.find('section', {'id': 'currentEpisode'})
title = latest_episode.find('h2', {'class': 'title'}).text
episode_onclick = latest_episode.findChildren('a')[0]['onclick']
onclick_split = episode_onclick.split(',')[2]
episode_id = onclick_split.split('_')[1].replace("'","")
latest_episode_link = "https://www.stitcher.com/podcast/uhh-yeah-dude/e/" + episode_id

line = title + ' - ' + latest_episode_link
print(line)

# Write to a file maybe?
# with open("uyd-episode-list.txt", "a") as file_object:
#     file_object.write(line)

