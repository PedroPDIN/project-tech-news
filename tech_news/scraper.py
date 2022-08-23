import requests
import time


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


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == '__main__':
  print(fetch('https://blog.betrybe.com/'))