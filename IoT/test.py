from urllib import request, parse
import json
import  time
'''
url = 'http://127.0.0.1:8000/login/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = [
    ('username','admin'),
    ('password','admin'),
]
headers = { 'User-Agent' : user_agent }
data = parse.urlencode(values).encode("utf-8")
req = request.Request(url, data, headers)
with request.urlopen(req, data=data) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

url = 'http://127.0.0.1:8000/add1/'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
'''
values = [
    ('name','456'),
    ('phonenumber','123'),
    ('email','qqfq@qq.com'),
    ('qq','7777'),
    ('address','beijing')
]'''
while(True):
    time.sleep(5)
    values = [
    ('SN','39'),
    ('sn','900'),
    ('tem','56'),
    ('alarm','qqq'),
    ('op','ook')
    ]
    #headers = { 'User-Agent' : user_agent }
    data = parse.urlencode(values).encode("utf-8")
    req = request.Request(url, data)
    request.urlopen(req, data=data)
'''
with request.urlopen(req, data=data) as f:
    #print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''

'''
f=request.urlopen(req, data=data)
jsondata =  f.read().decode('utf-8')
j=json.loads(jsondata)
print(j['check'])
print(j)
'''

