from autoscraper import AutoScraper

url = 'https://finance.yahoo.com/quote/AAPL/'

wanted_list = ["138.20"]

scraper = AutoScraper()

# Here we can also pass html content via the html parameter instead
# of the url (html=html_content)
result = scraper.get_result_exact('https://finance.yahoo.com/quote/MSFT/') 
print(result)
