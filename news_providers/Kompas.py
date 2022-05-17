import requests
from DateHelper import setDateTime
from bs4 import BeautifulSoup


class Kompas:

    def __init__(self):
        self.headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        self.baseUrl = "https://www.kompas.com/tag/"

    def getNews(self, data, keywords):
        for keyword in keywords:
            req = requests.get(self.baseUrl+keyword, self.headers)
            doc = BeautifulSoup(req.content, "html.parser")
            try:
                newsContainer = doc.find_all('div', class_="article__list")
                if newsContainer:
                    for news in newsContainer:
                        datetime = news.find(class_="article__date").string
                        datetime = datetime.replace(
                            '/', '-').replace(',', '').replace(' WIB', '')

                        title = news.find(class_="article__link").text
                        link = news.find(class_="article__link")['href']
                        image = news.find('img')['src']
                        datetime = setDateTime(datetime, '%d-%m-%Y %H:%M')

                        data.append({
                            "title": title,
                            "link": link,
                            "image": image,
                            "datetime": datetime,
                            "keyword": keyword,
                            "source": "KOMPAS"
                        })
            except:
                continue
        return data
