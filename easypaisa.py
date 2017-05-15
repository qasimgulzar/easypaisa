import httplib, urllib
host = 'easypaystg.easypaisa.com.pk'
url = '/easypay/Index.jsf'
values = {
    'storeId' : '5623',
    'amount' : '10',
    'postBackURL' : 'http://www.my.online-store.com/transaction/MessageHandler',
    'orderRefNum' : '1101'
}
headers = {
    'User-Agent': 'python',
    'Content-Type': 'application/x-www-form-urlencoded',
}
values = urllib.urlencode(values)
conn = httplib.HTTPSConnection(host)
conn.request("POST", url, values, headers)
response = conn.getresponse()
data = response.read()

print(data)