import asyncio
import aiohttp

async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.text()
            
async def main():
    await fetch_html("https://example.com")
asyncio.run(main())