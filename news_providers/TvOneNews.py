import requests
from DateHelper import setDateTime
from bs4 import BeautifulSoup


class TvOneNews:

    def __init__(self):
        self.headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        self.baseUrl = "https://www.tvonenews.com/tag/"

    def getNews(self, data, keywords):
        for keyword in keywords:
            req = requests.get(self.baseUrl+keyword, self.headers)
            doc = BeautifulSoup(req.content, "html.parser")
            try:
                newsContainer = doc.find(
                    'div', class_="site-container-big").find_all("div", class_="article-list-row")
                if(newsContainer):
                    for news in newsContainer:
                        linkData = news.find(class_="alt-link")
                        detailData = news.find(class_="ali-title")
                        dateData = news.find(class_="ali-date")
                        dateString = dateData.span.string

                        title = detailData.h2.text
                        link = linkData["href"]
                        image = linkData.img["data-original"]
                        dateFormat = '%d/%m/%Y - %H:%M' if ' - ' in dateString else '%d/%m/%Y'
                        datetime = setDateTime(
                            dateString, dateFormat)

                        data.append({
                            "title": title,
                            "link": link,
                            "image": image,
                            "datetime": datetime,
                            "keyword": keyword,
                            "source": "TV ONE NEWS"
                        })
            except:
                continue
        return data
