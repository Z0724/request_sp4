# 抓取PTT的網頁原始碼
import urllib.request as req

def getData(url):
    # 建立request物件，附加header資訊
    request=req.Request(url ,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response :
        data=response.read().decode("utf-8")

    # # 檢析原始碼，取得文章標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser") # 讓BS4協助解析html
    titles=root.find_all("div", class_="title") # 尋找所有class="title 的div標籤
    for title in titles :
        if title.a != None : # 如果標題包含 a 標籤，《印出來
            print(title.a.string)
    nextlink=root.find("a", string="‹ 上頁") # 搜尋內文是上頁的 a 標籤
    return nextlink["href"] # 從搜尋結果抓網址

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3 : #抓 N 頁標題
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1






