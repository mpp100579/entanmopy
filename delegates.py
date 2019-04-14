#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import http_helper as http

_kPaths = {
    # get
    'count': '/api/delegates/count',
    # get
    'getVoters': '/api/delegates/voters',
    # get
    'getDelegate': '/api/delegates/get',
    # get
    'getDelegates': '/api/delegates',
    # get
    'getFee': '/api/delegates/fee',
    # get
    'getForgedByAccount': '/api/delegates/forging/getForgedByAccount',
    # put
    'addDelegate': '/api/delegates',
    # put
    'delDelegate': '/api/delegates/undelegate'
}


def count(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['count'], timeout=timeout)


def getVoters(nodeServer, publicKey, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getVoters'], {'publicKey': publicKey}, timeout=timeout)


def getDelegate(nodeServer, publicKey=None, username=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {}
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    if username != None:
        reqArgs['username'] = username
    assert(len(reqArgs) > 0, 'Invalid arguments')
    return http.get(nodeServer+_kPaths['getDelegate'], reqArgs, timeout=timeout)


def getDelegates(nodeServer, offset=0, limit=100, address=None, orderBy=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'offset': offset, 'limit': limit}
    _orderByFilters = ["username", "address", "publicKey", "balance", "vote", "rewards",
                       "fees", "producedblocks", "missedblocks", "rate", "approval", "productivity", "forged"]
    if address != None:
        reqArgs['address'] = address
    if orderBy != None:
        reqArgs['orderBy'] = orderBy
    return http.get(nodeServer+_kPaths['getDelegates'], reqArgs, timeout=timeout)


def getFee(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getFee'], timeout=timeout)


def getForgedByAccount(nodeServer, generatorPublicKey, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getForgedByAccount'], {'generatorPublicKey': generatorPublicKey}, timeout=timeout)


def addDelegate(nodeServer, secret, username, publicKey=None, secondSecret=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'secret': secret, 'username': username}
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    if secondSecret != None:
        reqArgs['secondSecret'] = secondSecret
    return http.put(nodeServer+_kPaths['addDelegate'], reqArgs, timeout=timeout)


def delDelegate(nodeServer, secret, publicKey=None, secondSecret=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'secret': secret}
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    if secondSecret != None:
        reqArgs['secondSecret'] = secondSecret
    return http.put(nodeServer+_kPaths['delDelegate'], reqArgs, timeout=timeout)
