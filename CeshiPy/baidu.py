# -*- coding: utf-8 -*-
import urllib.request, json

url = 'http://apis.baidu.com/netpopo/illegaladdr/coord?lat=31.3004088721&lng=121.4849729860&range=2000&num=10'
add_header = {"apikey": "9a1bfb513e18XXXXXf48314508e"}
req = urllib.request.Request(url, headers=add_header)
resp = urllib.request.urlopen(req)
content = resp.read().decode('utf-8')
# 不用.decode('utf-8'）会报错the JSON object must be str, not 'bytes'
res = json.loads(content)
if (res):
    print(res)