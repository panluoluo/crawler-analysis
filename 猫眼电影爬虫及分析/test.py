urls = ['https://maoyan.com/board/4?offset={}'.format(str(i)) for i in range(0,100,10)]
for url in urls:
    print(url)