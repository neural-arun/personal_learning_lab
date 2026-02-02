

import asyncio
import aiohttp

urls = [
    "https://example.com",
"https://httpbin.org/html",
"https://quotes.toscrape.com",
"https://books.toscrape.com",
"https://news.ycombinator.com",
"https://jsonplaceholder.typicode.com/posts",
"https://jsonplaceholder.typicode.com/users",
"https://www.wikipedia.org",
"https://httpbin.org/delay/2",
"https://httpbin.org/headers",

]

# yahan sirf fetch_html ka skeleton

async def fetch_html(session,url,sem):
    async with sem:
        async with session.get(url) as response:
            return await response.text()
    
async def main():
    sem = asyncio.Semaphore(3)
    async with aiohttp.ClientSession() as session:
        html_str_as_list = []
        tasks = []
        for url in urls:
            task = fetch_html(session,url,sem)
            tasks.append(task)
        html_str_as_list = await asyncio.gather(*tasks,return_exceptions=True)
        print(len(html_str_as_list))
        return html_str_as_list
result = asyncio.run(main())
print(result)
