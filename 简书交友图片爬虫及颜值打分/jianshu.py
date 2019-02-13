import requests
from lxml import etree
import time

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

path = 'https://www.jianshu.com'

def get_url(url):
    res = requests.get(url,headers=headers)
    html = etree.HTML(res.text)
    infos = html.xpath('//ul[@class="note-list"]/li')
    for info in infos:
        href = info.xpath('div/a/@href')[0]
        det_url = path + href
        print(det_url)
        get_img(det_url)
    time.sleep(2)

def get_img(url):
    i = 1
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    title = html.xpath('/html/body/div[1]/div[2]/div[1]/h1/text()')[0].strip('|').split('，')[0].split('/')[0]
    id = html.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span/a/text()')[0]
    # print(title,id)
    infos = html.xpath('//div[@class="image-package"]')
    for info in infos:
        img_url = 'http:' + info.xpath('div[1]/div[2]/img/@data-original-src')[0]
        print(img_url)
        res_1 = requests.get(img_url,headers=headers)
        fp = open('row_img/' + title + '+' + id + '+' + str(i) + '.jpg','wb')
        fp.write(res_1.content)
        i = i + 1


if __name__ == '__main__':
    urls = ['https://www.jianshu.com/c/bd38bd199ec6?order_by=added_at&page={}'.format(str(i)) for i in range(1,10)]
    for url in urls:
        get_url(url)