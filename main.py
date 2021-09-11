import requests
from bs4 import BeautifulSoup as bs
import time

WEBHOOK = 'https://discord.com/api/webhooks/Example-Webhook'
SEARCH_TERM = 'python'
SEARCH_TERM_ICON = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png'

for cycle in range(10):
    cycle += 1
    response = requests.get(url=f"https://www.upwork.com/search/jobs/t/1/?page={cycle}&q={SEARCH_TERM}&sort=recency&visitor_pref=1", headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"})
    soup = bs(response.content, "html.parser")
    counter = 0
    for i in soup.find_all('a'):
        if i.parent.name == 'h4':
            title = (i.find("up-c-line-clamp").text)
            desc = (soup.find_all('span', {"class":"js-description-text"})[counter].text[0:(soup.find_all('span', {"class":"js-description-text"})[counter].text.find('.') + 1)] + " (...)\n\n\n\n")
            link = soup.find_all("a", {"class":"job-title-link break visited"})[counter]['href']
            strong = soup.find_all("strong", {"class":"js-budget"})[counter]
            price = strong.find("span").text.strip()
            xp = soup.find_all("strong", {"class":"js-contractor-tier"})[counter].text
            link = f'https://www.upwork.com/freelance-jobs/apply{link[4:]}'

            payload = {
    "content": None,
    "embeds": [
        {
        "title": title,
        "description": f"```\n{desc}```",
        "url": link,
        "color": 2020100,
        "fields": [
            {
            "name": "Fixed Price",
            "value": price,
            "inline": True
            },
            {
            "name": "Experience Level",
            "value": xp,
            "inline": True
            }
        ],
        "author": {
            "name": f"Upwork scraper | {(SEARCH_TERM).capitalize()}",
            "icon_url": SEARCH_TERM_ICON
        }
        }
    ],
    "username": "Upwork",
    "avatar_url": "https://assets-global.website-files.com/5ec7d9f13fc8c0ec8a4c6b26/6092b794e0419d97d9b06e2b_Favicon%20256.png"
    }
            send = requests.post(WEBHOOK, json=payload)
            counter += 1
            time.sleep(0.3)
