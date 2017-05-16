import httplib2, urllib
host = 'easypay.easypaisa.com.pk'
url = '/easypay/Index.jsf'
values = {
    'storeId' : '5623',
    'amount' : '12',
    'postBackURL' : 'https://easypaisa.herokuapp.com/postbackhandler/',
    'orderRefNum' : '1101',
    'expiryDate' : '20140606 201521'
}
headers = {
    'User-Agent': 'python',
    'Content-Type': 'application/x-www-form-urlencoded',
}
values = urllib.parse.urlencode(values)
conn = httplib2.HTTPSConnectionWithTimeout(host,timeout=1000)
conn.request("POST", url, values, headers)
response = conn.getresponse()
data = response.read()
