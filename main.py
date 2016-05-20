from BeautifulSoup import BeautifulSoup, BeautifulStoneSoup
from support import config, htmlcap
import httplib, urllib, json, os.path

def stringclean(input_string):
    return ' '.join(input_string.split())

def update_log():
    with open(log, 'w') as f:
        json.dump(order_status, f, sort_keys=True, indent=4, ensure_ascii=False)

def pushmessage(title,message):
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
        "token": config.pushover()[0],
        "user": config.pushover()[1],
        "message": message,
        "title": title,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

def findfromindex(find_index,dict):
    temp_index = 0
    for entry in dict:
        temp_index += 1
        if temp_index == find_index:
            return entry

log = './log.json'

html = htmlcap.findmyorder(config.ordernumber(),config.password())

soup = BeautifulSoup(html)
p = soup.findAll('p')
order_status = {}

order_status.update({'status':stringclean(findfromindex(config.search_index(),p).string)})
order_status.update({'info':stringclean(findfromindex(config.search_index()+1,p).string)})

if os.path.isfile(log):
    pass
else:
    update_log()
    pushmessage(order_status['status'], order_status['info'])
    exit()
with open(log) as data_file:
    log_order_status = json.load(data_file)
if log_order_status['status'] != order_status['status']:
    update_log()
    pushmessage(order_status['status'],order_status['info'])
    exit()
if log_order_status['info'] != order_status['info']:
    update_log()
    pushmessage(order_status['status'],order_status['info'])