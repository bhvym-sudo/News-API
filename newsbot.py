import feedparser
import requests
from bs4 import BeautifulSoup
import re
import json

def fetch_rss_bbc():
    feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(feed_url)
    
    articles = []
    for entry in feed.entries:
        articles.append({"title": entry.title, "link": entry.link})
    return articles

    

    


def fetch_nytimes_rss():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    feed = feedparser.parse(feed_url)

    articles = []
    for entry in feed.entries:
        articles.append({"region": "World","title": entry.title, "link": entry.link, "description": entry.description})

    return articles


def fetch_nytimes_africa():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"region": "Africa","title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_nytimes_americas():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"region": "America","title": entry.title, "link": entry.link, "description": entry.description})
    return articles


def fetch_nytimes_asiapac():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/AsiaPacific.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"region": "Asiapacific","title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_nytimes_europe():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"region": "Europe","title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_nytimes_middleast():
    feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml"
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        articles.append({"region": "MiddleEast","title": entry.title, "link": entry.link, "description": entry.description})
    return articles

def fetch_all_nytimes_news():
    # regions = {
    #     "World": fetch_nytimes_rss(),
    #     "Africa": fetch_nytimes_africa(),
    #     "Americas": fetch_nytimes_americas(),
    #     "Asia Pacific": fetch_nytimes_asiapac(),
    #     "Europe": fetch_nytimes_europe(),
    #     "Middle East": fetch_nytimes_middleast(),
    # }
    regions = {
        "World": fetch_nytimes_rss()
    }

    all_articles = []
    for region, articles in regions.items():
        for article in articles:
            all_articles.append({
                "region": region,
                "title": article["title"],
                "link": article["link"],
                "description": article["description"]
            })

    return all_articles

def get_rusuk_cnn():
    r = requests.get("https://edition.cnn.com/world/europe/ukraine")
    soup = BeautifulSoup(r.content, "html.parser")
    d = soup.find("div",class_="container__field-links container_list-headlines__field-links")
    data = d.text.splitlines()
    fil = [item for item in data if item]
    return fil

def search_cnn():
    d = input("Enter your query: ").strip()
    forr = "+".join(d.split())
    
    r = requests.get(f"https://www.bbc.com/search?q={forr}&edgeauth=eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJrZXkiOiAiZmFzdGx5LXVyaS10b2tlbi0xIiwiZXhwIjogMTczODM1MDI0MSwibmJmIjogMTczODM0OTg4MSwicmVxdWVzdHVyaSI6ICIlMkZzZWFyY2glM0ZxJTNEZWR3YXJkJTI1MjBzbm93ZGVuIn0.pL1mcrv5_-McqDWjEqpFx-5yyBwMbbmZknW0A0Ypi8E")
    soup = BeautifulSoup(r.content, "html.parser")
    df = soup.find_all("div", class_="sc-c6f6255e-0 eGcloy")
    dta = []
    for elements in df:
        dta.append(elements.text)


    pattern = re.compile(r'(.+?)(\d{1,2} \w+ \d{4}|\d+ day[s]? ago)([A-Za-z &]+)?$')

    for article in dta:
        match = pattern.search(article)
        if match:
            content = match.group(1).strip().rstrip('.')
            date = match.group(2).strip()
            location = match.group(3).strip() if match.group(3) else "N/A"  # Handle missing location
            print(f"Content: {content}\nDate: {date}\nLocation: {location}\n")
        else:
            print(f"❌ Failed to match: {article}\n")


def search_timeofindia():
    d = input("Enter your query: ").strip()
    forr = "-".join(d.split())
    r = requests.get(f'https://toifeeds.indiatimes.com/treact/feeds/toi/web/show/topic?path=/topic/{forr}/news&row=20 &curpg=1')
    data = r.json()
    total_count = data['contentsData']['totalcount']
    print(total_count)
    items = data['contentsData']['items']
    for item in items:
        hl = item.get('hl', 'N/A')
        syn = item.get('syn', 'N/A')
        print(hl)
        print(syn)
        print()






