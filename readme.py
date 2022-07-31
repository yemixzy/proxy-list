import json

README = """
# Free HTTP Proxy List 🌍

Free Proxy List for everyone

> Scraper found **{NUMBER_OF_TOTAL_PROXIES}** proxies at the latest update. Usable proxies are below.

## Usage

Click the file format that you want and copy the URL.


|File|Content|Count|
|----|-------|-----|
|[not_checked.txt]({GITHUB_RAW_URL}/proxy-list/not_checked.txt)|`ip_address:port` combined (seperated new line)|{NUMBER_OF_TOTAL_PROXIES}|
|[data.txt]({GITHUB_RAW_URL}/proxy-list/data.txt)|`ip_address:port` combined (seperated new line)|{NUMBER_OF_USABLE_PROXIES}|
|[data.json]({GITHUB_RAW_URL}/proxy-list/data.json)|`ip, port`|{NUMBER_OF_USABLE_PROXIES}|
|[data-with-geolocation.json]({GITHUB_RAW_URL}/proxy-list/data-with-geolocation.json)|`ip, port, geolocation`|{NUMBER_OF_USABLE_GEO_PROXIES}|

## Sources

|Source|Found Proxies|Succeed|
|------|-------------|-------|
{SOURCES}

"""  # noqa

GITHUB_RAW_URL = 'https://raw.githubusercontent.com/yemixzy/proxy-list/main'  # noqa


def update_readme(metrics: dict):
    global README
    global GITHUB_RAW_URL

    SOURCES_MD = ''
    template = '|{}|{}|{}|\n'
    for x in metrics['sources']:
        source = f'[{x.get("id")}]({x.get("url")})'
        found_proxies = x['count']
        succeed = x['succeed']
        if succeed:
            succeed = '✅'
        else:
            succeed = '🚫'
        SOURCES_MD += template.format(source, found_proxies, succeed)

    PROXY_LIST_MD = ''
    if metrics['counts']['geolocation'] > 0:
        template = '|{row_num}|{ip}|{port}|{country}|{city}|{isp}|\n'
        with open('proxy-list/data-with-geolocation.json', 'r') as f:
            geolocations = json.load(f)
            formatted = []
            for i, x in enumerate(geolocations, 1):
                tmp = dict((k, v) for k, v in dict(x["geolocation"]).items())
                tmp["ip"] = x["ip"]
                tmp["port"] = x["port"]
                tmp['row_num'] = i
                formatted.append(tmp)
                if i == 20:
                    break

            for x in formatted:
                PROXY_LIST_MD += template.format(**x)
    else:
        PROXY_LIST_MD = '**Something went wrong... Check the actions logs.**'

    data = {
        'SOURCES': SOURCES_MD,
        'PROXY_LIST': PROXY_LIST_MD,
        'GITHUB_RAW_URL': GITHUB_RAW_URL,
        'NUMBER_OF_TOTAL_PROXIES': str(metrics['counts']['found']),
        'NUMBER_OF_USABLE_PROXIES': str(metrics['counts']['usable']),
        'NUMBER_OF_USABLE_GEO_PROXIES': str(metrics['counts']['geolocation']),
    }

    with open('README.md', 'w') as f:
        f.write(README.format(**data))
