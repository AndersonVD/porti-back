from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def mercadoLivre(busca):
    query = busca.replace(' ', '-')
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path='C:/Users/ander/Documents/Programas/portifolio/porti-back/chromedriver.exe', options=chrome_options)
    driver.get(f'https://lista.mercadolivre.com.br/{query}')
    for i in range(0, 6):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(0.5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    div_items = soup.findAll(
        'li', attrs={'class': 'ui-search-layout__item shops__layout-item'})

    itens = []
    for item in range(1, 10):
        try:
            _id = item
            link = div_items[item].find(
                'a', class_='ui-search-link')['href']
            if link[0:4] == "data":
                continue
            title = div_items[item].find(
                'h2', class_='ui-search-item__title').text
            price = div_items[item].find(
                'span', class_='andes-money-amount__fraction').text
            image = div_items[item].find(
                'img', class_='ui-search-result-image__element')['src']
            itens.append({"id": _id, 'title': title, 'price': price,
                          'image': image, 'link': link})
        except:
            continue
    return itens


if __name__ == '__main__':
    mercadoLivre()
