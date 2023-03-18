import requests
from bs4 import BeautifulSoup


def justwatch():
    # query = busca.replace(' ', '%20')
    page = requests.get('https://www.justwatch.com/br/busca?q=vingadores')

    soup = BeautifulSoup(page.text, 'html.parser')
    div_items = soup.findAll('div', class_="title-list-row__row")

    itens = []
    for item in range(len(div_items)):
        title = div_items[item].find('span', class_="header-title").text
        image = div_items[item].find('img')['src']
        link = "https://www.justwatch.com" + \
            div_items[item].find('a')['href']
        itens.append(
            {'title': title, 'image': image, 'link': link}
        )

    return print(itens)


if __name__ == '__main__':
    justwatch()
