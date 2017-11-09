# -*-*-
# 感谢骚男 『zh (QQ: 315393472)』 提供的源代码
# -*-*-

# ! -*- encoding:utf-8 -*-

import requests

# 要访问的目标页面
targetUrl = "http://ditu.amap.com/detail/get/detail?id=B023B02GYJ"
# targetUrl = "http://proxy.abuyun.com/switch-ip"
# targetUrl = "http://proxy.abuyun.com/current-ip"

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "HN5861W41O905A0D"
proxyPass = "044A1683F60BB0C2"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

resp = requests.get(targetUrl, proxies=proxies)

print(resp.status_code)
print(resp.text)
