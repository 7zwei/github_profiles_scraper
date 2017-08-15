# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_proxies():
    soup = BeautifulSoup(get_html('https://free-proxy-list.net/'), 'lxml')
    proxies = []
    prx = []
    for i in soup.findAll('td'):
        proxies.append(i.text)
    for k in range(1, int(len(proxies)/8)):
        prx.append(proxies[0::8][k] + ":"+proxies[1::8][k])
    return prx[:50]

def get_user_agents():
    return open('ua.txt').read().split('\n')