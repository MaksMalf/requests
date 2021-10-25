import requests
from pprint import pprint

url_list = ["https://superheroapi.com/api/2619421814940190/search/Hulk",
            "https://superheroapi.com/api/2619421814940190/search/Captain%America",
            "https://superheroapi.com/api/2619421814940190/search/Thanos"]


def test_request(urls):
    res = (requests.get(url) for url in urls)
    return res
    

def result():
    heroes = []
    for item in test_request(url_list):
        intelligence = item.json()
        pprint(intelligence)
        try:
            for power_stats in intelligence['results']:
                heroes.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence']
                    })
        except KeyError:
            print(f"Проверь url_list: {url_list}")

    intelligence_heroes = 0
    name = ''
    for intelligence_hero in heroes:
        if intelligence_heroes < int(intelligence_hero['intelligence']):
            intelligence_heroes = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый умный: {name}, интелект: {intelligence_heroes}")



if __name__ == '__main__':
    test_request(url_list)
    result()