import requests


def get_html(url):
    try:
        result = requests.get(url)
    # по умолчанию exception возвращается только если произошла какая-то фатальная ошибка
    # 404 , 505 и т.д. - вернет содержание этих страниц.
    # для того, чтобы при получении таких страниц возвращалась ошибка:
        result.raise_for_status()        
        return result.text
    # все exceptions в библиотеке реквестс наследуются от одного класса
    except requests.exceptions.RequestException:
        print('Sorry, something goes wrang')
        return False

if __name__ == '__main__':
    print(get_html('https://learn.python.ru/lessons/5_db.html?full#2'))