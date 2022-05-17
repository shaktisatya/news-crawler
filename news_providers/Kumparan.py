from datetime import datetime, timedelta
import locale
import requests
from bs4 import BeautifulSoup


class Kumparan:

    def __init__(self):
        self.headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        self.baseUrl = "https://kumparan.com/topic/"

    def getNews(self, data, keywords):
        for keyword in keywords:
            req = requests.get(self.baseUrl+keyword, self.headers)
            doc = BeautifulSoup(req.content, "html.parser")
            try:
                newsContainer = doc.select('div[data-qa-id="news-item"]')
                if newsContainer:
                    for news in newsContainer:
                        image = news.select('div[data-qa-id="image"]')
                        dateText = news.select(
                            'a[data-qa-id="comment-button-wrapper"]')[0].find_next_sibling().string

                        title = news.span.text
                        link = 'https://kumparan.com/'+news.a['href']
                        image = image[0].img['src']
                        datetime = self.setDateTime(dateText)
                        data.append({
                            "title": title,
                            "link": link,
                            "image": image,
                            "datetime": datetime,
                            "keyword": keyword,
                            "source": "KUMPARAN"
                        })
            except:
                continue
        return data

    def setDateTime(self, dateText):
        dateText = dateText.replace('Ags', 'Agu')
        dateText = dateText.strip()
        try:
            if dateText == 'sedetik':
                retData = datetime.now() - timedelta(seconds=1)

            elif dateText == 'semenit':
                retData = datetime.now() - timedelta(minutes=1)

            elif dateText == 'sejam':
                retData = datetime.now() - timedelta(hours=1)

            elif 'detik' in dateText:
                getNum = dateText.replace(' detik', '')
                retData = datetime.now() - timedelta(seconds=int(getNum))

            elif 'menit' in dateText:
                getNum = dateText.replace(' menit', '')
                retData = datetime.now() - timedelta(minutes=int(getNum))

            elif 'jam' in dateText:
                getNum = dateText.replace(' jam', '')
                retData = datetime.now() - timedelta(hours=int(getNum))

            else:
                locale.setlocale(locale.LC_ALL, 'id_ID')
                retData = datetime.strptime(dateText, '%d %b %Y')
        except Exception as e:
            retData = datetime.now()
        finally:
            retData = retData.strftime('%d-%m-%Y %H:%M:00')
        return retData
