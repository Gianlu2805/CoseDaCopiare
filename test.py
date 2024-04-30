import json
import requests

proxy_servers = {
    'http': "http://s_lrcfnc06e03f240n:pippococa:@10.0.0.1:800",
    # 'https': "https://@10.0.0.1:800"
}

request_server = "http://10.25.0.14:3000"


def get_data():
    response = requests.get(request_server, proxies=proxy_servers)

    if response.status_code == 200:
        data = response.text
        print(data)
    else:
        print("An error occured: %d", response.status_code)


def make_post_request():
    url = 'http://10.25.0.15:10000/postListener'
    myobj = {'somekey': 'somevalue'}

    x = requests.post(url, json=myobj, proxies=proxy_servers)

    print(x.text)


if __name__ == "__main__":
    make_post_request()
