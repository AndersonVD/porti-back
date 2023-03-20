import requests
from bs4 import BeautifulSoup


def g1():
    page = requests.get('https://g1.globo.com/busca/?q=bbb')

    soup = BeautifulSoup(page.text, 'html.parser')
    div_items = soup.findAll(
        'li', class_="widget widget--card widget--info")

    itens = []
    for item in range(1, 10):
        try:
            _id = item
            title = div_items[item].find(
                'div', class_="widget--info__title product-color").text.replace('\n', '').strip()
            time_ago = div_items[item].find(
                'div', class_="widget--info__meta").text
            image = "https:" + div_items[item].find('img')['src']
            link = "https:" + div_items[item].find('a')['href']
            itens.append(
                {"id": _id, 'title': title, 'time_ago': time_ago,
                    'image': image, 'link': link}
            )
        except:
            continue

    return itens


if __name__ == '__main__':
    g1()
