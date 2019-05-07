#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import http_helper as http

_kPaths = {
    # get
    'getLockVote': '/api/lockvote/get',
    # get
    'getAllLockVotes': '/api/lockvote/all',
    # put
    'add': '/api/lockvote',
    # put
    'remove': '/api/lockvote/remove'
}


def getLockVote(nodeServer, trid, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getLockVote'], {'id': trid}, timeout=timeout)


def getAllLockVotes(nodeServer, address, offset=0, limit=100, state=None, orderByHeight=None, orderByAmount=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'address': address, 'offset': offset, 'limit': limit}
    if state != None:
        reqArgs['state'] = state
    if orderByHeight != None:
        reqArgs['orderByHeight'] = orderByHeight
    if orderByAmount != None:
        reqArgs['orderByAmount'] = orderByAmount
    return http.get(nodeServer+_kPaths['getAllLockVotes'], reqArgs, timeout=timeout)


def add(nodeServer, secret, amount, publicKey=None, secondSecret=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'secret': secret, 'args': [''+amount]}
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    if secondSecret != None:
        reqArgs['secondSecret'] = secondSecret
    return http.put(nodeServer+_kPaths['add'], reqArgs, timeout=timeout)


def remove(nodeServer, secret, trids=[], publicKey=None, secondSecret=None, timeout=4000):
    # TODO: check arguments
    if isinstance(trids, list):
        reqArgs = {'secret': secret, 'args': trids}
    elif isinstance(trids, str):
        reqArgs = {'secret': secret, 'args': [trids]}
    else:
        reqArgs = {'secret': secret, 'args': []}
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    if secondSecret != None:
        reqArgs['secondSecret'] = secondSecret
    return http.put(nodeServer+_kPaths['remove'], reqArgs, timeout=timeout)
