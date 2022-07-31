SOURCES = [
    {
        "id": "free-proxy-list.net",
        "url": "https://free-proxy-list.net",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "us-proxy.org",
        "url": "https://www.us-proxy.org",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxydb.net",
        "url": "http://proxydb.net",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": None,
                "port": None,
                "combined": "Proxy",
            },
        }
    },
    {
        "id": "free-proxy-list.com",
        "url": "https://free-proxy-list.com/?page=&port=&type%5B%5D=http&type%5B%5D=https&up_time=0&search=Search",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 1,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxy-list.download",
        "url": "https://www.proxy-list.download/HTTP",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP Address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "vpnoverview.com",
        "url": "https://vpnoverview.com/privacy/anonymous-browsing/free-proxy-servers",
        "method": "GET",
        "parser": {
            "pandas": {
                "table_index": 0,
                "ip": "IP address",
                "port": "Port",
                "combined": None,
            },
        }
    },
    {
        "id": "proxyscrape.com",
        "url": "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/clarketm/proxy-list",
        "url": "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/monosans/proxy-list",
        "url": "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/TheSpeedX/PROXY-List",
        "url": "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/almroot/proxylist",
        "url": "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/ShiftyTR/Proxy-List",
        "url": "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/mmpx12/proxy-list/http",
        "url": "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/mmpx12/proxy-list/https",
        "url": "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/clarketm/proxy-list",
        "url": "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
    {
        "id": "github.com/jetkai/proxy-list",
        "url": "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        "method": "GET",
        "parser": {
            "txt": {},
        }
    },
]
