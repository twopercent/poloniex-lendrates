#!/usr/bin/env python3

import configparser
import requests
import urllib
import hmac
import hashlib
import time
import base64
import json

PUBLIC_API = 'https://poloniex.com/public?command='
TRADING_API = 'https://poloniex.com/tradingApi'
LOAN_CURRENCY = 'BTC', 'BTS', 'CLAM', 'DOGE', 'DASH', 'LTC', 'MAID', 'STR', 'XMR', 'XRP', 'ETH', 'FCT'

KeyInfo = configparser.ConfigParser()
KeyInfo.read('poloniex.ini')

class poloniex:
    def __init__(self):
        self.APIKey = KeyInfo.get('poloniex', 'APIKey')
        self.Secret = KeyInfo.get('poloniex', 'Secret')

    def api_query(self, command, req={}):
        req['command'] = command
        req['nonce'] = int(time.time()*1000)
        post_data = urllib.parse.urlencode(req)

        sign = hmac.new(self.Secret, post_data, hashlib.sha512).hexdigest()
        headers = {
            'Sign': sign,
            'Key': self.APIKey
        }

        print(post_data)
        print(sign)

#        ret = urllib2.urlopen(urllib2.Request('https://poloniex.com/tradingApi', post_data, headers))
#        jsonRet = json.loads(ret.read())
#        return(jsonRet)

    def loan_orders(self, currency):
        r = requests.get(PUBLIC_API + 'returnLoanOrders&currency=' + currency)
        return(r.text)

    def test(self):
        print(self.APIKey)

if __name__ == '__main__':
    myPo = poloniex()

    data = myPo.loan_orders('BTC')
    json_data = json.loads(data)
#    print(json.dumps(json_data, indent=4))
#    print(type(json_data))
#    print(json_data['offers'])
#    print(type(json_data['offers']))

    for curr in LOAN_CURRENCY:
        data = myPo.loan_orders(curr)
        json_data = json.loads(data)
        print(curr + ' .' + json_data['offers'][0]['rate'][4:8])


    #for i in range(len(json_data['offers'])):
    #    print(i)
    #    print(json_data['offers'][i])
#    print(myPo.loan_orders('BTC'))
#    print(myPo.loan_orders('MAID'))
#    myPo.api_query('returnActiveLoans')
#    print(base64.b16decode(myPo.Secret))

