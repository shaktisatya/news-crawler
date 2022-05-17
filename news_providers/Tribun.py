from datetime import datetime, timedelta
import locale
import requests
from bs4 import BeautifulSoup
from sqlalchemy import true


class Tribun:

    def __init__(self):
        self.headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

        self.baseUrl = "https://www.tribunnews.com/tag/"

    def getNews(self, data, keywords):
        for keyword in keywords:
            req = requests.get(self.baseUrl+keyword, self.headers)
            doc = BeautifulSoup(req.content, "html.parser")
            try:
                newsContainer = doc.find('ul', class_="lsi").find_all('li')
                if(newsContainer):
                    for news in newsContainer:
                        title = news.find('a', class_="fbo")['title'].text
                        link = news.find('a', class_="fbo")['href']
                        image = news.find('img')['src']
                        datetime = self.setDateTime(news.find('time').string)

                        data.append({
                            "title": title,
                            "link": link,
                            "image": image,
                            "datetime": datetime,
                            "keyword": keyword,
                            "source": "TRIBUN"
                        })
            except:
                continue
        return data

    def setDateTime(self, dateText):
        locale.setlocale(locale.LC_ALL, 'id_ID')
        try:
            if 'detik lalu' in dateText:
                getNum = dateText.replace(' detik lalu', '')
                retData = datetime.now() - timedelta(seconds=int(getNum))

            elif 'menit lalu' in dateText:
                getNum = dateText.replace(' menit lalu', '')
                retData = datetime.now() - timedelta(minutes=int(getNum))

            elif 'jam lalu' in dateText:
                getNum = dateText.replace(' jam lalu', '')
                retData = datetime.now() - timedelta(hours=int(getNum))

            elif 'hari lalu' in dateText:
                getNum = dateText.replace(' hari lalu', '')
                retData = datetime.now() - timedelta(days=int(getNum))

            else:
                dateText = dateText.split(', ')
                dateText = dateText[1].split(' ')
                if(int(dateText[0]) < 9):
                    dateText[0] = '0'+dateText[0]
                dateText = dateText[0]+' '+dateText[1]+' '+dateText[2]
                retData = datetime.strptime(dateText, '%d %B %Y')
        except:
            retData = datetime.now()
        finally:
            retData = retData.strftime('%d-%m-%Y %H:%M:00')
        return retData
