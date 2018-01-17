# coding=utf-8

import json
import requests

PAGE_SIZE = 10
URL = 'http://mp.hudoufun.cn/tenement/js/listview_h5.ashx?' \
      'op=1' \
      '&r=0.6620256237220019' \
      '&table=tenement_rooms1' \
      '&city=%E6%88%90%E9%83%BD&lng=0' \
      '&lat=0' \
      '&filter=' \
      '&order2=auto' \
      '&PADDING=0' \
      '&refable=false' \
      '&page=js%2Flistview_h5.ashx' \
      '&search=' \
      '&order=' \
      '&totalnum=-1' \
      '&random=0.3783954663667828'
def getWeb(url):
    print('Fetching URL: ' + url)
    requests.session()
    resp = requests.get(url)
    resp.encoding='utf-8'
    html = resp.text

    return html

def fetch(pageIndex, pageSize):
    url = URL + '&pageindex=' + str(pageIndex) + '&pageSize=' + str(pageSize)
    content = getWeb(url)
    result = json.loads(content)
    #print(result)
    return result

def readHudouOnlineData():
    pageIndex = 0
    hasPage = True
    houses = []
    while (hasPage) :
        result = fetch(pageIndex, PAGE_SIZE)
        houses = houses + result['data']
        pageIndex = pageIndex + 1
        hasPage = True if(pageIndex < int(result['pagenum'])) else False
    soldCount = 0
    totalPrice = 0.0
    for house in houses:
        if(int(house['sold']) == 1):
            soldCount = soldCount + 1
            totalPrice = totalPrice + float(house['price4hour'])
    print('\n总房屋间夜: ' + str(len(houses)) +
          '\n已售间夜: ' + str(soldCount) +
          #'\n销售额: ' + str(round(totalPrice,2)) +
          '\n销售额（优惠后）: ' + str(round(totalPrice*0.88, 2)))
    return

#readHudouOnlineData()