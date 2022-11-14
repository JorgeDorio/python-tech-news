import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url: str):
    try:
        headers = {"user-agent": "Fake user-agent"}
        fetch = requests.get(url, headers=headers)
        time.sleep(1)
        if fetch.status_code == 200:
            return fetch.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html: str):
    selector = Selector(text=html)
    urls = selector.css(".cs-overlay-link::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html: str):
    selector = Selector(html)
    return selector.css(".next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_noticia(html):
    selector = Selector(html)
    result = {}
    result["url"] = selector.css('link[rel="canonical"]::attr(href)').get()
    result["title"] = selector.css(".entry-title::text").get().strip()
    result["timestamp"] = selector.css(".meta-date::text").get()
    result["writer"] = selector.css(".author>.url.fn.n::text").get()
    result["comments_count"] = len(selector.css(".comment-list>li").getall())
    result["summary"] = "".join(
        selector.css(".entry-content>p:nth-of-type(1) ::text").getall()
    ).strip()
    result["tags"] = selector.css(".post-tags a::text").getall()
    result["category"] = selector.css(".meta-category .label::text").get()
    return result


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
