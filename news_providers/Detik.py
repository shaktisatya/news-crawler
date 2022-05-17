import requests
from DateHelper import setDateTime
from bs4 import BeautifulSoup


class Detik:

    def __init__(self):
        self.headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        self.baseUrl = "https://www.detik.com/tag/"

    def getNews(self, data, keywords):
        for keyword in keywords:
            req = requests.get(self.baseUrl+keyword, self.headers)
            doc = BeautifulSoup(req.content, "html.parser")
            try:
                newsContainer = doc.find_all("article")
                if newsContainer:
                    for news in newsContainer:
                        dateData = news.find(
                            'span', class_="date").get_text().split(', ')[1].replace(' WIB', '')

                        title = news.find('h2', class_="title").text
                        link = news.find('a')["href"]
                        image = news.find('img')['src']
                        datetime = setDateTime(dateData)

                        data.append({
                            "title": title,
                            "link": link,
                            "image": image,
                            "datetime": datetime,
                            "keyword": keyword,
                            "source": "DETIK"
                        })
            except:
                continue

        return data
