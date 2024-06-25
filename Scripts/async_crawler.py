import asyncio
from concurrent.futures import ThreadPoolExecutor
from http.client import HTTPSConnection
from urllib.parse import urlparse, urljoin
from html.parser import HTMLParser
from typing import Set

#parser class
class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    self.links.append(value)

def fetch_page_sync(url: str) -> str:
    url_parts = urlparse(url)
    connection = HTTPSConnection(url_parts.netloc)
    connection.request("GET", url_parts.path or '/')
    response = connection.getresponse()
    return response.read().decode('utf-8') if response.status == 200 else ""

async def fetch_page(url: str) -> str:
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, fetch_page_sync, url)

# extract links from HTML 
def extract_links(html: str, base_url: str) -> Set[str]:
    parser = LinkExtractor()
    parser.feed(html)
    return {urljoin(base_url, link) for link in parser.links}

# crawl function
async def crawl(start_url: str, max_depth: int, visited: Set[str] = None):
    if visited is None:
        visited = set()
    if start_url in visited or max_depth < 0:
        return
    visited.add(start_url)
    html = await fetch_page(start_url)
    links = extract_links(html, start_url)
    print(f"Visited: {start_url}")
    await asyncio.gather(*(crawl(link, max_depth - 1, visited) for link in links if link not in visited))


if __name__ == "__main__":
    start_url = 'https://ganjoor.net/'
    max_depth = 2
    asyncio.run(crawl(start_url, max_depth))
