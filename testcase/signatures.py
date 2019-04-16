#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import http_helper as http

_kPaths = {
    # put
    'add': '/api/signatures',
    # get
    'getFee': '/api/signatures/fee'
}


def add(nodeServer, secret, secondSecret, publicKey=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'secret': secret, 'secondSecret': secondSecret}
    if publicKey != None:
        reqArgs['publicKey'] = publicKey
    return http.put(nodeServer+_kPaths['add'], reqArgs, timeout=timeout)


def getFee(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getFee'], timeout=timeout)
