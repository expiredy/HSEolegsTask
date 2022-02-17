import requests
from bs4 import BeautifulSoup


request_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.46 (Edition Yx GX)"
}


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # request and grab content
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    # to store proxies
    proxies = []
    for row in soup.find("tbody"):
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    return proxies


def get_soup_respose_from_request(request_url, new_request_proxies):
    response = requests.get(url=request_url, headers=request_headers, proxies=new_request_proxies)
    response_soup = BeautifulSoup(response.text, "lxml")
    return response_soup


def show_api_addres():
    response_soup = get_soup_respose_from_request("https://2ip.ru")
    ip_addres = response_soup.find("div", class_="ip").text.strip()
    print("current ip addres: ", ip_addres)


def request_vote(proxies):
    try:
        response_soup = get_soup_respose_from_request("https://mostbeautyboy.ru/contests/roman-novikov5", proxies)
        print("A")
    except:
        print("Not Available")
        return

    vote_button = response_soup.find("div", class_="btn add_voice").text.strip()


'''
doing a randomized colldown between requests, to make it less suspicious
'''
def artificial_cooldown() -> None:
    from time import sleep
    from random import randint

    sleep(randint(1, 10))


def main():
    proxies = get_free_proxies()
    print(proxies)
    for element in range(len(proxies)):
        request_vote(proxies={"http": element, "https": element})

    # show_api_addres()
    # send_request("https://2ip.ru")
    # send_request("https://mostbeautyboy.ru/contests/roman-novikov5")
    # send_request("https://mostbeautyboy.ru/js/general.js?1609489383")
    # vote_with_current_ip()

if __name__ == '__main__':
    main()