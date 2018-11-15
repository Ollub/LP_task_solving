import requests as rq

def get_weather(url):
    result = rq.get(url)
    if rq.status_code == 200:
        return result.json()
    else:
        print('Something goes wrong!')