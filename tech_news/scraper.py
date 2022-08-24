import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(
          url,
          headers={"User-Agent": "Fake user-agent"},
          timeout=3
        )
        time.sleep(1)

        if response.status_code != 200:
            return None

        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    all_urls = selector.css(
      '.entry-title a::attr(href)'
    ).getall()
    return all_urls


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url_next = selector.css('.next::attr(href)').get()
    return url_next


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url_links = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css('.entry-title::text').get().strip()
    date = selector.css('.meta-date::text').get()
    author = selector.css('.author a::text').get()
    all_comments = selector.css('#comment').getall()
    tags = selector.css("a[rel='tag']::text").getall()
    category = selector.css('.label::text').get()
    fist_comment = selector.xpath(
      "string(.//div[@class='entry-content']/p)"
    ).get().strip()

    dist_noticia = {
      'url': url_links,
      'title': title,
      'timestamp': date,
      'writer': author,
      'comments_count': len(all_comments),
      'summary': fist_comment,
      'tags': tags,
      'category': category,
    }

    return dist_noticia


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    # 852 urls
    url_base = 'https://blog.betrybe.com/'
    links_noticias = []
    dist_noticias = []

    while len(links_noticias) <= amount:
        for link in scrape_novidades(fetch(url_base)):
            links_noticias.append(link)
        url_base = scrape_next_page_link(fetch(url_base))

    for link in links_noticias[:amount]:
        dist_noticias.append(scrape_noticia(fetch(link)))

    create_news(dist_noticias)
    return dist_noticias
