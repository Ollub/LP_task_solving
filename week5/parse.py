from bs4 import BeautifulSoup

from req import get_html

html = get_html('https://yandex.ru/search/?text=python&lr=213')
# вторым аргументом передается парсер
if html:    
    bs = BeautifulSoup(html, 'html.parser')
    search_block = []
    for item in bs.find_all('li', class_='serp-item'):
        block_header = item.find('div', class_='organic__url-text')
        block_link = item.find('a', class_='path__item').get('href')
        search_block.append({
                        'header': block_header.text,
                        'link': block_link
                            })
    else:
        print('could not get html')

if search_block:
    for block in search_block:
        for key, value in block.items():
            print( key, value)
        print('*'*10)

# with open('presentation.txt', 'w', encoding='utf-8') as file:
#     file.write(bs.prettify().encode('utf-8'))
