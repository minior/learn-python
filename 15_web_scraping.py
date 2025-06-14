import bs4
import requests

# script to scrape amazon (or any shopping link's) product price
res = requests.get("https://www.amazon.com/Nutribullet-Superfood-Nutrition-Extractor-NBR-0601/dp/B07CTBHQZK/?th=1")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser") # soup is just random object created
    # html.parser arg avoids innocuous error message
elements = soup.select("#corePriceDisplay_mobile_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.a-price.aok-align-center.reinventPricePriceToPayMargin.priceToPay > span:nth-child(2) > span.a-price-whole")
    # select() returns a LIST of elements
print(elements[0].text.strip()) #.text is just calling a PROPERTY of the elements object
 
#note: might not work cause amazon blocks bots nowadays
 