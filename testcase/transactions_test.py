#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import transactions

_nodeServer = 'http://39.105.210.35:5000'
_secret='race forget pause shoe trick first abuse insane hope budget river enough'
_recipientId='AMFcPgkRndYVgjMs9gKTKMEwW72yGivw3z'
_delayTimestamp='["1938485755"]'

if __name__ == "__main__":
    print('getTransactions', transactions.getTransactions(_nodeServer, limit=1))
    print('getTransactions', transactions.getTransactions(_nodeServer, limit=2, orderBy='blockHeight:desc'))
    print('getTransaction', transactions.getTransaction(_nodeServer, trid='f0af7052a760edb104c118d1f6950f597f50a314b872508d9bc7e16f7062219c'))
    print('getUnconfirmedTransactions',transactions.getUnconfirmedTransactions(_nodeServer,senderPublicKey='', address=''))
    print('addTransactions',transactions.add(_nodeServer,_secret, _recipientId, 10000))
    print('addDelayTransactions',transactions.addDelay(_nodeServer,_secret, _recipientId, _delayTimestamp,10000))