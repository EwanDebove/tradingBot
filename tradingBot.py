# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:25:43 2020

@author: Ewan Debove
"""

import requests

r=requests.get('https://api.coinbase.com/v2/currencies')

response = r.json()

currencies=[]

for i in range(len(response['data'])):
    currencies.append(response['data'][i]['name'])
    
print(currencies)