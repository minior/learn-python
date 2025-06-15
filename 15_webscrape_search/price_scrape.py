# function to get price of product

import bs4, requests

def get_price(url, css_selector):
    res = requests.get(url)
    res.raise_for_status()
    #select price part
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elements = soup.select(css_selector)
    return elements[0].text.strip()

url = "https://shopee.sg/%F0%9F%87%B8%F0%9F%87%AC64-cubes-Stackable-Ice-Cube-Maker-Tray-Quick-Releasewith-Ice-Storage-Box-with-Lid-Ice-Cube-Tray-Mold-Ice-Jelly-Mold-i.748753155.18692434099?sp_atk=bfe0d7d6-3dfc-4ede-8888-612a2414cd27&xptdk=bfe0d7d6-3dfc-4ede-8888-612a2414cd27"
css_selector = "#sll2-normal-pdp-main > div > div > div > div.container > section > section.flex.flex-auto.YTDXQ0 > div > div:nth-child(3) > div.flex.flex-column.IFdRIb > section > div > div.IZPeQz.B67UQ0"
price = get_price(url, css_selector)
print ('Price now is ' + price)

# again, most stores use JS so doesnt work, requests.get() retrieves RAW HTML