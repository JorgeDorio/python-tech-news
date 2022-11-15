from datetime import datetime


# Requisito 6
from tech_news.database import search_news


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    result = []
    for new in news:
        result.append((new["title"], new["url"]))

    return result


# Requisito 7
def search_by_date(date: str):
    try:
        time = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        news = search_news({"timestamp": time})
        result = []
        for new in news:
            result.append((new["title"], new["url"]))
        return result
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
