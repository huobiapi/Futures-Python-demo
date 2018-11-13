#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:48:13 2018

@author: zhaobo
"""

from HuobiDMService import HuobiDM
from pprint import pprint

#### input huobi dm url
URL = ''

####  input your access_key and secret_key below:
ACCESS_KEY = ''
SECRET_KEY = ''


dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

#### another account:
#dm2 = HuobiDM(URL, "ANOTHER ACCOUNT's ACCESS_KEY", "ANOTHER ACCOUNT's SECRET_KEY")




#%%  market data api ===============

print (u' 获取合约信息 ')
pprint (dm.get_contract_info(symbol="BTC", contract_type="quarter"))
pprint (dm.get_contract_info(contract_code="BTC181228"))

print (u' 获取合约指数信息 ')
pprint (dm.get_contract_index("BTC"))

print (u' 获取合约最高限价和最低限价 ')
pprint (dm.get_contract_price_limit(symbol='BTC', contract_type='quarter'))
pprint (dm.get_contract_price_limit(contract_code='BTC181228'))

print (u' 获取当前可用合约总持仓量 ')
pprint (dm.get_contract_open_interest(symbol='BTC', contract_type='quarter'))
pprint (dm.get_contract_open_interest(contract_code='BTC181228'))

print (u' 获取行情深度数据 ')
pprint (dm.get_contract_depth(symbol='BTC_CW', type='step0'))

print (u' 获取K线数据 ')
pprint (dm.get_contract_kline(symbol='BTC_CW', period='60min', size=20))

print (u' 获取聚合行情 ')
pprint (dm.get_contract_market_merged('BTC_CW'))

print (u' 获取市场最近成交记录 ')
pprint (dm.get_contract_trade('BTC_CW'))

print (u' 批量获取最近的交易记录 ')
pprint (dm.get_contract_batch_trade(symbol='BTC_CW', size=3))



#%% trade / account api  ===============

print (u' 获取用户账户信息 ')
pprint (dm.get_contract_account_info())
pprint (dm.get_contract_account_info("BTC"))

print (u' 获取用户持仓信息 ')
pprint (dm.get_contract_position_info())
pprint (dm.get_contract_position_info("BTC"))

print (u' 合约下单 ')
pprint(dm.send_contract_order(symbol='', contract_type='', contract_code='BTC181228', 
                        client_order_id='', price=10000, volume=1, direction='sell',
                        offset='open', lever_rate=5, order_price_type='limit'))


print (u' 合约批量下单 ')
orders_data = {'orders_data': [
               {'symbol': 'BTC', 'contract_type': 'quarter',  
                'contract_code':'BTC181228',  'client_order_id':'', 
                'price':10000, 'volume':1, 'direction':'sell', 'offset':'open', 
                'leverRate':5, 'orderPriceType':'limit'},
               {'symbol': 'BTC','contract_type': 'quarter', 
                'contract_code':'BTC181228', 'client_order_id':'', 
                'price':20000, 'volume':2, 'direction':'sell', 'offset':'open', 
                'leverRate':5, 'orderPriceType':'limit'}]}
pprint(dm.send_contract_batchorder(orders_data))


print (u' 撤销订单 ')
pprint(dm.cancel_contract_order(symbol='BTC', order_id='42652161'))

print (u' 全部撤单 ')
pprint(dm.cancel_all_contract_order(symbol='BTC'))

print (u' 获取合约订单信息 ')
pprint(dm.get_contract_order_info(symbol='BTC', order_id='42652161'))

print (u' 获取合约订单明细信息 ')
pprint(dm.get_contract_order_detail(symbol='BTC', order_id='42652161', order_type=1, created_at=1542097630215))

print (u' 获取合约当前未成交委托 ')
pprint(dm.get_contract_open_orders(symbol='BTC'))

print (u' 获取合约历史委托 ')
pprint (dm.get_contract_history_orders(symbol='BTC', trade_type=0, type=1, status=0, create_date=7))




