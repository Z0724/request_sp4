import requests
from bs4 import BeautifulSoup
import urllib.request as req


url = "https://invoice.etax.nat.gov.tw/index.html"
# html = requests.get(url=url)
# html.encoding = 'utf_8_sig'
# print(html.text)
# sp = BeautifulSoup(html.text,'html.parser')

request=req.Request(url)
with req.urlopen(request) as response :
    data=response.read().decode("utf-8")
print(data)
# date1 = sp.select('div', {'class':'container-fluid etw-bgbox mb-4'})