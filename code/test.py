import requests
import bs4
import random

url = "http://www.ip181.com/"
proxiess = {
  "http": "http://27.40.141.142:61234",
  "http": "http://61.152.230.26:8080",
  "http": "http://222.125.32.206:8080",
  "http": "http://123.57.76.102:80",
}
response = requests.get(url);
soup=bs4.BeautifulSoup(response.text);
table=soup.select('tr');
proxies = {
}
ipList=[];
for tr in table:
    ip="http://"+tr.get_text().split()[0]+":"+tr.get_text().split()[1];
    ipList.append(ip);

length=len(ipList);
ableList=[];
for proxy in ipList:
    proxies={'http':'http://'+proxy};
    print(proxies);
    try:
        r=requests.get(url,proxies=proxiess,timeout=3);
        print(r);
        if r.status_code == 200 :
            print(proxy);
            ableList.append(proxy);
    except:
        print("此代理无效");
print(ableList);







