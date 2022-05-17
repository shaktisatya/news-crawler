import requests
from DateHelper import setDateTime
from bs4 import BeautifulSoup


class PrfmNews:

    def __init__(self):
        self.headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        self.baseUrl = "https://prfmnews.pikiran-rakyat.com/tag/"

    def getNews(self, data, keywords):
        for keyword in keywords:
            keyword = keyword.title()
            req = requests.get(self.baseUrl+keyword, self.headers)
            doc = BeautifulSoup(req.content, "html.parser")
            try:
                newsContainer = doc.find('div', class_="latest__wrap").find_all(
                    "div", class_="latest__item")
                for news in newsContainer:
                    dateData = news.date.string.replace(' WIB', '')

                    title = news.find('a', class_="latest__link").text
                    link = news.find('a')['href']
                    image = news.find('img')['src']
                    datetime = setDateTime(dateData, '%d %B %Y, %H:%M')

                    data.append({
                        'title': title,
                        'link': link,
                        'image': image,
                        'datetime': datetime,
                        "keyword": keyword,
                        'source': 'PRFM NEWS'
                    })
            except:
                continue
        return data
