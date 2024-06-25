import asyncio
import json
from http.client import HTTPSConnection
from typing import List
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

def fetch_data_sync(url: str) -> dict:
    url_parts = urlparse(url)
    connection = HTTPSConnection(url_parts.netloc)
    connection.request("GET", url_parts.path)
    response = connection.getresponse()

    if response.status == 200:
        data = response.read()
        return json.loads(data)
    else:
        print(f"Failed to fetch data from {url}: {response.status}")
        return {}

async def fetch_data(url: str) -> dict:
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, fetch_data_sync, url)

async def main(urls: List[str]) -> List[dict]:
    tasks = [fetch_data(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    return responses

urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3'
]

if __name__ == "__main__":
    results = asyncio.run(main(urls))
    for result in results:
        print(result)
