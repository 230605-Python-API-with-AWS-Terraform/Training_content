import http.client
req=http.client.HTTPConnection('www.google.com',80,timeout=10)
req.request("GET","/")
res=req.getresponse()
gethead=res.getheaders()
print(gethead)
print(res.reason)
print(res.status)
req.close()