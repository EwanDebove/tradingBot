# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:25:43 2020

@author: Ewan Debove
"""

import requests
import json
import urllib
import datetime
import time
import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('data.db')
c = conn.cursor()



def getNames():
    r=requests.get('https://api-public.sandbox.pro.coinbase.com/currencies')
    
    response = r.json()
    
    currencies=[]
    
    for i in range(len(response)):
        currencies.append(response[i]['name'])
        
    print(currencies)

  
def getDepth(direction, pair):
    
    r = requests.get(  "https://api.pro.coinbase.com/products/"+pair+"/book")
    
    response = r.json()
    if (direction == "ask"):
        print(response['asks'][0][1])
    if (direction == "bid"):
        print(response['bids'][0][1])

    
    
def getOrderBook(asset):
 
    r=requests.get("https://api.pro.coinbase.com/products/"+asset+"/book?level=2")

    response = r.json() 

    print(response)


def refreshDataCandles(pair, duration):


    start = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=duration)
    start = start.isoformat()
    start=urllib.parse.quote(start)
   
    end = datetime.datetime.now(datetime.timezone.utc).isoformat()
    end = urllib.parse.quote(end)

    url = "https://api.pro.coinbase.com/products/BTC-USD/candles?start="+start+"&end="+end
    r=requests.get(url)
    response = r.json()

    print(response)
    
    createTable()
    data_entry(lastId() + 1, 'Coinbase', pair, duration, 'data.db', str(lastCheck()), start, lastId())



def createTable():
    c.execute("CREATE TABLE IF NOT EXISTS last_checks(Id INTEGER PRIMARY KEY, exchange TEXT, trading_pair TEXT, duration TEXT, table_name TEXT, last_check INT, startdate INT, last_id INT)")


def data_entry(Id, exchange, trading_pair, duration, table_name, last_check, startdate, last_id):
    c.execute("INSERT INTO last_checks VALUES(Id, exchange, trading_pair, duration, table_name, last_check, startdate, last_id)")
    conn.commit()
    c.close()
    conn.close()
 
def lastId():
    c.execute('SELECT MAX(last_id) FROM last_checks')
    data = c.fetchall()
    return(data[0][0])
def lastCheck():
    c.execute('SELECT * FROM last_checks ORDER BY ID DESC LIMIT 1 ')
    data = c.fetchall()
    return(data)
