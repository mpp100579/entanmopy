#!/usr/bin/env python 
# -*- encoding: utf-8 -*-

import accounts

_nodeServer = 'http://39.105.210.35:5000'

_genesisSecret = 'fluid bracket forum either face bird toy april boss stamp february pencil'
_genesisPublicKey = '220ca36be9d82e9b88abf25d2bdf8de9fd858f381a3cbd5a01d20a1637f28835'
_genesisAddress = 'AKEfwcTExJ4NZZ9C5o3P7q5mQcrvuL9vAi'

if __name__ == "__main__":
    accounts.addDelegates(_nodeServer, _genesisSecret, remove='a08dc0d7b170a0e12caff0a7faaef952741e65f3585905a5847e4d877d650f07')
    resp = accounts.new(_nodeServer, ent=128)
    print('new', resp)
    if resp['done'] == True:  #如果返回结果为true,
        _newSecret = resp['data']['secret']   #获取新建账号返回结果中的地址和公钥
        _newPublicKey = resp['data']['publicKey']
        _newAddress = resp['data']['address']
        print('open', accounts.open(_nodeServer, _newSecret))
        print('open2', accounts.open2(_nodeServer, _newPublicKey))
        print('getBalance', accounts.getBalance(_nodeServer, _newAddress))
        print('getPublicKey', accounts.getPublicKey(_nodeServer, _newAddress))
        print('generatePublicKey', accounts.generatePublicKey(_nodeServer, _newSecret))
        print('getDelegates', accounts.getDelegates(_nodeServer, _newAddress))
        print('getAccount', accounts.getAccount(_nodeServer, _newAddress))
        print('accountOnChain', accounts.accountOnChain(_nodeServer, _newAddress))
        print('delayOrders', accounts.delayOrders(_nodeServer, _newAddress))
        print('delayOrders', accounts.delayOrders(_nodeServer, _newAddress, 1))

    print('===========================================')
    print('open', accounts.open(_nodeServer, _genesisSecret))
    print('open2', accounts.open(_nodeServer, _genesisPublicKey))
    print('getBalance', accounts.getBalance(_nodeServer, _genesisAddress))
    print('getPublicKey', accounts.getPublicKey(_nodeServer, _genesisAddress))
    print('generatePublicKey', accounts.generatePublicKey(_nodeServer, _genesisSecret))
    print('getDelegates', accounts.getDelegates(_nodeServer, _genesisAddress))
    print('getDelegateFee', accounts.getDelegateFee(_nodeServer))
    print('getAccount', accounts.getAccount(_nodeServer, _genesisAddress))
    print('accountOnChain', accounts.accountOnChain(_nodeServer, _genesisAddress))
    print('delayOrders', accounts.delayOrders(_nodeServer, _genesisAddress))
    print('top', accounts.top(_nodeServer, limit=10))
    print('top', accounts.top(_nodeServer, offset=8, limit=2))
    print('count', accounts.count(_nodeServer))