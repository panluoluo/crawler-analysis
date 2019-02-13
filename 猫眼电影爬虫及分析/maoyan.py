import requests
from lxml import etree
import csv
# import time

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

def get_url(url):
    res = requests.get(url,headers=headers)
    # print(res.text)
    html = etree.HTML(res.text)
    infos = html.xpath('//dl[@class="board-wrapper"]/dd')
    for info in infos:
        title = info.xpath('div/div/div[1]/p[1]/a/text()')[0]
        author = info.xpath('div/div/div[1]/p[2]/text()')[0].strip().strip('主演：')
        pub_time = info.xpath('div/div/div[1]/p[3]/text()')[0].strip('上映时间：')
        star_1 = info.xpath('div/div/div[2]/p/i[1]/text()')[0]
        star_2 = info.xpath('div/div/div[2]/p/i[2]/text()')[0]
        star = star_1 + star_2
        movie_url = 'https://maoyan.com' + info.xpath('div/div/div[1]/p[1]/a/@href')[0]
        # print(title,author,pub_time,star,movie_url)
        get_info(movie_url,title,author,pub_time,star)

def get_info(url,title,author,pub_time,star):
    res = requests.get(url, headers=headers)
    html = etree.HTML(res.text)
    style = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/text()')[0]
    long_time = html.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[2]/text()')[0].split('/')[1].strip().strip('分钟')
    print(title,author,pub_time,star,style,long_time)
    writer.writerow([title,author,pub_time,star,style,long_time])

if __name__ == '__main__':
    fp = open('maoyan.csv','w',newline='',encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(['title','author','pub_time','star','style','long_time'])
    urls = ['https://maoyan.com/board/4?offset={}'.format(str(i)) for i in range(0,100,10)]
    for url in urls:
        get_url(url)