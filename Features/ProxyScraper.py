from Features.base import FeatureBase
import proxyscrape
import time
import requests
from bs4 import BeautifulSoup
from proxy_checker import ProxyChecker
from proxyscrape.shared import Proxy

collecotr = 1
proxy_checker = ProxyChecker()

#Adding more proxy websites
def request_proxy_list(url):
    try:
        response = requests.get(url)
    except requests.RequestException:
        return False

    if not response.ok:
        return False
    return response

def get_socks4_US_proxy():
    url="https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=7000&country=us&anonymity=elite&ssl=all"
    response = request_proxy_list(url)
    try:
        soup = BeautifulSoup(response.content, 'html.parser')
        proxies = set()
        data = str(soup).splitlines()

        for proxy in data:
            host = proxy.split(':')[0]
            port = proxy.split(':')[1]
            proxies.add(Proxy(host, port, 'us', 'united states', True, 'socks4', 'proxyscrape'))

        return proxies
    except (AttributeError, KeyError):
        return False

proxyscrape.add_resource('proxyscrape', get_socks4_US_proxy, 'socks4')

class Feature(FeatureBase):
    def __init__(self):
        super().__init__(
            name="Proxy Scraper",
            description="This is a proxy scraper",
            options=[
                {
                    "message": "Amount: ",
                    "type": "input",
                    "name": 'amount'
                },
                {
                    "message": "Type: ",
                    "type": "list",
                    "choices": ['HTTP', 'Socks4', 'Socks5', 'all'],
                    'name': 'type'
                },
                {
                    "message": "Country: ",
                    "type": "checkbox",
                    "choices": [{
                        "name": "us"
                    }, 
                    {
                        "name": "uk"
                    }, 
                    {
                        "name": "ca"
                    },
                    {
                        "name": 'all'
                    }],
                    "name": 'country'
                },
                {
                    "message": "Anonymous: ",
                    "type": "confirm",
                    "name": "anonymous"
                },
                {
                    "message": "File to save to: ",
                    "type": 'input',
                    "name": 'file_name'
                }
            ]
        )

    def function(self, options):
        global collecotr
        proxy_list = []
        f = open(options["file_name"], 'a')
        collecotr+=1
        print('Gathering Proxys...')
        if options['type'] == 'all':
            collector = proxyscrape.create_collector(f"Collector-{collecotr}", ['http','https','socks4','socks5'])
        else:
            collector = proxyscrape.create_collector(f"Collector-{collecotr}", options['type'].lower())
        collector.refresh_proxies()
        for i in range(int(options['amount'])):
            if options['country'] == ['all']:
                proxy = collector.get_proxy({'anonymous': options['anonymous']})
            else:
                proxy = collector.get_proxy({'code': options['country'], 'anonymous': options['anonymous']})
            if proxy == None:
                print("Failed to get set amount of proxys")
                break

            proxy_list.append(proxy)
            f.write(f"{proxy.host}:{proxy.port}\n")
            collector.blacklist_proxy(proxy)
            print(f"{i+1}. {proxy.host}:{proxy.port}:{proxy.type}:{proxy.country}")
        collector.clear_blacklist()
        f.close()
        input('Press enter to return to main screen.')