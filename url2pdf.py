import asyncio
from pyppeteer import launch

async def generate_pdf(url, pdf_path):
    browser = await launch()
    page = await browser.newPage()
    
    await page.goto(url)
    
    await page.pdf({'path': pdf_path, 'format': 'A4'})
    
    await browser.close()

# Run the function
url = ''
output_file = "C:\\test\\example.pdf"
asyncio.get_event_loop().run_until_complete(generate_pdf(url, output_file))

C:\Software\github.com\mehrdad-zade