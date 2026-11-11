import requests
from bs4 import BeautifulSoup


def fetch_page():
    url = " https://www.mercadolivre.com.br/impressora-3d-flashforge-creator-5-com-4-bicos-multicolor-cinza/p/MLB80160087?pdp_filters=item_id%3AMLB5393031771#polycard_client=search-desktop&be_origin=searchv2&overlay_label=not_apply&search_layout=grid&position=3&type=product&tracking_id=04c8c691-cfa2-42cf-8ddf-8abddc542c27&overlay_label_capability=not_apply&wid=MLB5393031771&sid=search"
    response = requests.get(url)
    return response.text

def parse_page(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    product_name = soup.find('h1', class_='ui-pdp-title').get_text()
    old_price = soup.find('span', class_='price-tag-previous-value')
    if old_price:
        old_price = old_price.get_text()
    else:
        old_price = "No previous price available"
    
    price = soup.find_all('span', class_='price-tag-fraction').get_text()
    print(f"Price: {price}")
    print(f"Old Price: {old_price}")




if __name__ == "__main__":
    content = fetch_page()
    products = parse_page(html_content=content)
    
    
    