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

log = 'log.json'

html = htmlcap.findmyorder(config.ordernumber(),config.password())

soup = BeautifulSoup(html)
p = soup.findAll('p')
search = "Order Status:"
index = 0
order_status = {}
printnext = False
for x in p:
    try:
        if x.string.find(search) and index <= 1:
            index += 1
            order_status.update({'status':stringclean(x.string)})
            printnext = True
        if printnext and x.string.find(search) == -1:
            printnext = False
            order_status.update({'info': stringclean(x.string)})
    except:
        continue
print(order_status)
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