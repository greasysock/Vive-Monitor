import json
import os.path
conf = os.path.dirname(os.path.dirname(__file__))+'/conf.json'
if os.path.isfile(conf):
    pass
else:
    configprep = dict()
    configprep['pushover'] = {'program_token':'pushover application token here', 'user_token':'pushover user token here'}
    configprep['findmyorder'] = {'password':'enter findmyorder password here'}
    configprep['order'] = {'order_number':'enter htc vive order number here'}
    configprep['script config'] = {'p_search_index':'3'}
    with open(conf, 'w') as f:
        json.dump(configprep, f, sort_keys = True, indent = 4,ensure_ascii=False)
    print("Configure script! Configuration located at '"+ conf +"'...")
    exit()
#configuration parameter checker.
with open(conf) as data_file:
    data = json.load(data_file)
def pushover():
    return data['pushover']['program_token'], data['pushover']['user_token']
def password():
    return data['findmyorder']['password']
def ordernumber():
    return data['order']['order_number']
def search_index():
    return int(data['script config']['p_search_index'])