from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    all_news = search_news({'title': {'$regex': title, '$options': 'i'}})
    # print(all_news)
    data_new = []

    for new in all_news:
        data_new.append((new['title'], new['url']))

    return data_new


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    date_new = []
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        date_find = datetime.strftime(date_obj, '%d/%m/%Y')
        all_date = search_news({'timestamp': date_find})
        for new in all_date:
            date_new.append((new['title'], new['url']))
    except ValueError:
        raise ValueError('Data inválida')
    return date_new


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
