import requests
import pprint
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

titles = soup.select(".titleline > a")
votes = soup.select(".score")

def custom_hn(titles, votes):
    hn = []
    for index, item in enumerate(titles):
        title = item.getText()
        link = item.get("href", None)
        vote = votes[index].getText().replace(" points", "")
        if(int(vote) > 99):
            hn.append({"title": title, "link": link, "vote": vote})
    pprint.pprint(sorted(hn, key = lambda k:k["vote"], reverse = True))

custom_hn(titles, votes)