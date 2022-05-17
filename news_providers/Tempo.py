from DateHelper import setDateTime
import requests
from bs4 import BeautifulSoup


class Tempo:

    def __init__(self):
        self.headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        self.baseUrl = "https://www.tempo.co/tag/"

    def getNews(self, data, keywords):
        for keyword in keywords:
            req = requests.get(self.baseUrl+keyword, self.headers)
            doc = BeautifulSoup(req.content, "html.parser")
            try:
                newsContainer = doc.find('ul', class_="wrapper").find_all('li')
                if newsContainer:
                    for news in newsContainer:
                        dateText = news.span.string.replace(' WIB', '')
                        title = news.h2.text
                        link = news.a['href']
                        image = news.img['src']
                        datetime = setDateTime(dateText, '%d %B %Y %H:%M')
                        data.append({
                            "title": title,
                            "link": link,
                            "image": image,
                            "datetime": datetime,
                            "keyword": keyword,
                            "source": "TEMPO"
                        })
            except:
                continue
        return data
