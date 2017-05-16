import httplib2, urllib
host = 'easypaystg.easypaisa.com.pk'
url = '/easypay/Index.jsf'
values = {
    'storeId' : '2785',
    'amount' : '10',
    'postBackURL' : 'http://easypaisa.herokuapp.com/postbackhandler/',
    'orderRefNum' : '1101',
}
headers = {
    'User-Agent': 'python',
    'Content-Type': 'application/x-www-form-urlencoded',
}
values = urllib.parse.urlencode(values)
conn = httplib2.HTTPConnectionWithTimeout(host)
conn.request("POST", url, values, headers)
response = conn.getresponse()
data = response.read()