from flask import Flask, render_template
from news_providers.Detik import Detik
from news_providers.Kompas import Kompas
from news_providers.Kumparan import Kumparan
from news_providers.PrfmNews import PrfmNews
from news_providers.Tempo import Tempo
from news_providers.Tribun import Tribun
from news_providers.TvOneNews import TvOneNews

app = Flask(__name__)

keywords = [
    "ridwan-kamil",
    "jawa-barat",
    "jabar",
    "emil",
    "berita-jabar",
    "pemprov-jabar",
    "pemprov-jawa-barat",
]


@app.route('/')
def index():
    return render_template('index.html', nama="Shakti")


@app.route('/detik')
def detik():
    news = Detik()
    data = []
    news.getNews(data, keywords)
    return render_template('news.html', source="Detik", newsData=data)


@app.route('/kompas')
def kompas():
    news = Kompas()
    data = []
    news.getNews(data, keywords)
    return render_template('news.html', source="Kompas", newsData=data)


@app.route('/kumparan')
def kumparan():
    news = Kumparan()
    data = []
    news.getNews(data, keywords)
    return render_template('news.html', source="Kumparan", newsData=data)


@app.route('/prfm-news')
def prfmnews():
    news = PrfmNews()
    data = []
    news.getNews(data, keywords)
    return render_template('news.html', source="PRFM NEWS", newsData=data)


@app.route('/tempo')
def tempo():
    news = Tempo()
    data = []
    news.getNews(data, keywords)
    return render_template('news.html', source="Tempo", newsData=data)


@app.route('/tribun')
def tribun():
    news = Tribun()
    data = []
    news.getNews(data, keywords)
    return render_template('news.html', source="Tribun", newsData=data)


@app.route('/tvone-news')
def tvonenews():
    news = TvOneNews()
    data = []
    news.getNews(data, keywords)
    return render_template('news.html', source="TV One News", newsData=data)
