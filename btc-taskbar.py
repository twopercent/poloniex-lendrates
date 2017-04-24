#!/bin/env python3

import json
import requests

data = requests.get('https://poloniex.com/public?command=returnLoanOrders&currency=BTC')
json_data = json.loads(data.text)
print('Polo BTC .' + json_data['offers'][0]['rate'][4:8])
