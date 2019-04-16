#!/usr/bin/env python 
# -*- encoding: utf-8 -*-

import delegates 

_nodeServer = 'http://39.105.210.35:5000'

_genesisSecret = 'fluid bracket forum either face bird toy april boss stamp february pencil'
_genesisPublicKey = '220ca36be9d82e9b88abf25d2bdf8de9fd858f381a3cbd5a01d20a1637f28835'
_genesisAddress = 'AKEfwcTExJ4NZZ9C5o3P7q5mQcrvuL9vAi'


if __name__ == "__main__":
    print('count', delegates.count(_nodeServer))
    print('getDelegate', delegates.getDelegate(_nodeServer, publicKey=_genesisPublicKey))
    print('getDelegate', delegates.getDelegate(_nodeServer, username='etm_001'))
    print('getVoters', delegates.getVoters(_nodeServer, publicKey=_genesisPublicKey))
    print('getFee', delegates.getFee(_nodeServer))
    print('getForgedByAccount', delegates.getForgedByAccount(_nodeServer, generatorPublicKey=_genesisPublicKey))
    print('getDelegates', delegates.getDelegates(_nodeServer, address=_genesisAddress, limit=2))
    print('getDelegates', delegates.getDelegates(_nodeServer, limit=3))
    print('getDelegates', delegates.getDelegates(_nodeServer, offset=1, limit=2))
    print('getDelegates', delegates.getDelegates(_nodeServer, limit=3, orderBy='username:desc'))
    print('addDlegate',delegates.addDlegate(_nodeServer,secret=_genesisSecret,username='mpp1',publicKey=_genesisPublicKey)
    print('delDelegate',delegates.delDelegate(_nodeServer,secret=_genesisSecret)