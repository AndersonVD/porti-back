import requests
from bs4 import BeautifulSoup


def justwatch():
    # query = busca.replace(' ', '%20')
    page = requests.get('https://www.justwatch.com/br/busca?q=vingadores')

    soup = BeautifulSoup(page.text, 'html.parser')
    div_items = soup.findAll('div', class_="title-list-row__row")

    itens = []
    for item in range(len(div_items)):
        _id = item
        title = div_items[item].find('span', class_="header-title").text
        image = div_items[item].find('img')['src']
        link = "https://www.justwatch.com" + \
            div_items[item].find('a')['href']
        itens.append(
            {"id": _id, 'title': title, 'image': image, 'link': link}
        )

    return itens


if __name__ == '__main__':
    justwatch()
