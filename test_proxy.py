import requests

def open_file(path_file):
    proxy_list = []
    with open(path_file) as f:
        for proxies in f.readlines():
            proxy_list.append(proxies)
    return proxy_list

def save_list(list):
    with open('new_proxy.txt','w') as f:
        for new_proxy in list:
            f.write(new_proxy + '\n')

def run(url,time,path_file):
    new_list = []
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    for test_proxy in open_file(path_file):
        proxies = {
            'http': test_proxy,
            'https': test_proxy
        }
        r = requests.get(url,proxies=proxies,headers=header)
        proxy_time = r.elapsed.microseconds
        if proxy_time < time:
            new_list.append(proxies['http'])
    save_list(new_list)


if __name__ == '__main__':
    test_url = input('请输入测试的网站:')
    text_time = input('请输入设定延迟(毫秒):')
    path_file = input('请输入文本路径(把/全部改为\)')
    run(test_url,text_time,path_file)
