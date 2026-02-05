import requests
from typing import Optional, Dict, Any
from bs4 import BeautifulSoup

URLS = ['https://blog.cloudflare.com/r2-local-uploads/',
         'https://blog.cloudflare.com/uk-google-ai-crawler-policy/',
           'https://blog.cloudflare.com/vertical-microfrontends/',
             'https://blog.cloudflare.com/moltworker-self-hosted-ai-agent/',
               'https://blog.cloudflare.com/serverless-matrix-homeserver-workers/', 'https://blog.cloudflare.com/q4-2025-internet-disruption-summary/', 'https://blog.cloudflare.com/route-leak-incident-january-22-2026/', 'https://blog.cloudflare.com/acme-path-vulnerability/', 'https://blog.cloudflare.com/astro-joins-cloudflare/', 'https://blog.cloudflare.com/human-native-joins-cloudflare/', 'https://blog.cloudflare.com/cname-a-record-order-dns-standards/', 'https://blog.cloudflare.com/iran-protests-internet-shutdown/', 'https://blog.cloudflare.com/bgp-route-leak-venezuela/', 'https://blog.cloudflare.com/building-our-maintenance-scheduler-on-workers/', 'https://blog.cloudflare.com/fail-small-resilience-plan/', 'https://blog.cloudflare.com/h1-2025-transparency-report/', 'https://blog.cloudflare.com/r2-sql-aggregations/', 'https://blog.cloudflare.com/radar-2025-year-in-review/', 'https://blog.cloudflare.com/radar-2025-year-in-review-internet-services/', 'https://blog.cloudflare.com/react2shell-rsc-vulnerabilities-exploitation-threat-brief/']


def extract_title(html: str) -> Optional[str]:
    soup = BeautifulSoup(html, "lxml")

    h1 = soup.find("h1")
    if not h1:
        return None

    title = h1.get_text(strip=True)
    if not title:
        return None

    return title



def extract_publish_date(html: str) -> Optional[str]:
    soup = BeautifulSoup(html, "lxml")

    article = soup.find("article")
    if not article:
        return None

    p = article.find("p")
    if not p:
        return None

    date_text = p.get_text(strip=True)
    if not date_text:
        return None

    return date_text




def extract_authors(html: str) -> list[str]:
    soup = BeautifulSoup(html, "lxml")

    article = soup.find("article")
    if not article:
        return []

    authors = []

    ul = article.find("ul")
    if not ul:
        return authors

    for li in ul.find_all("li"):
        div = li.find("div")
        if not div:
            continue

        a = div.find("a")
        if not a:
            continue

        name = a.get_text(strip=True)
        if name:
            authors.append(name)

    return authors


def extract_article_text(html: str) -> Optional[str]:
    soup = BeautifulSoup(html, "lxml")

    article = soup.find("article")
    if not article:
        return None

    section = article.find("section")
    if not section:
        return None

    parts: list[str] = []

    for tag in section.find_all(["p", "h1", "h2", "h3"], recursive=True):
        text = tag.get_text(strip=True)
        if text:
            parts.append(text)

    if not parts:
        return None

    return "\n\n".join(parts)



def scrape_article(article_url: str) -> Optional[Dict[str, Any]]:
    try:
        response = requests.get(article_url, timeout=10)
        if response.status_code != 200:
            return None
        html = response.text

        article_data = {
            "url": article_url,
            "title": extract_title(html),
            "publish_date": extract_publish_date(html),
            "authors": extract_authors(html),
            "article_text": extract_article_text(html),
        }

        return article_data
    except requests.RequestException:
        return None
    

def scrape_articles(urls: list[str]) -> list[dict]:
    results = []

    for url in urls:
        data = scrape_article(url)
        if data:
            results.append(data)

    return results


