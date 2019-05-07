#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import http_helper as http

'''
'''

_kPaths = {
    # get
    'getBlock': '/api/blocks/get',
    # get
    'getFullBlock': '/api/blocks/full',
    # get
    'getBlocks': '/api/blocks',
    # get
    'getHeight': '/api/blocks/getHeight',
    # get
    'getFee': '/api/blocks/getFee',
    # get
    'getMilestone': '/api/blocks/getMilestone',
    # get
    'getReward': '/api/blocks/getReward',
    # get
    'getSupply': '/api/blocks/getSupply',
    # get
    'getStatus': '/api/blocks/getStatus'
}


def getBlock(nodeServer, blockid=None, height=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {}
    if blockid != None:
        reqArgs['id'] = blockid
    if height != None:
        reqArgs['height'] = height
    # assert(len(reqArgs) > 0, "Invalid arguments")
    return http.get(nodeServer+_kPaths['getBlock'], reqArgs, timeout=timeout)


def getFullBlock(nodeServer, blockid=None, height=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {}
    if blockid != None:
        reqArgs['id'] = blockid
    if height != None:
        reqArgs['height'] = height
    assert len(reqArgs) > 0, "Invalid arguments"
    return http.get(nodeServer+_kPaths['getFullBlock'], reqArgs, timeout=timeout)


def getBlocks(nodeServer, offset=0, limit=100, orderBy=None, height=None, generatorPublicKey=None, previousBlock=None, totalAmount=None, totalFee=None, reward=None, timeout=4000):
    # TODO: check arguments
    reqArgs = {'offset': offset, 'limit': limit}
    _orderByFilters = ["id", "timestamp", "height", "previousBlock", "totalAmount",
                       "totalFee", "reward", "numberOfTransactions", "generatorPublicKey"]
    if orderBy != None:
        reqArgs['orderBy'] = orderBy
    if height != None:
        reqArgs['height'] = height
    if generatorPublicKey != None:
        reqArgs['generatorPublicKey'] = generatorPublicKey
    if previousBlock != None:
        reqArgs['previousBlock'] = previousBlock
    if totalAmount != None:
        reqArgs['totalAmout'] = totalAmount
    if totalFee != None:
        reqArgs['totalFee'] = totalFee
    if reward != None:
        reqArgs['reward'] = reward
    return http.get(nodeServer+_kPaths['getBlocks'], reqArgs, timeout=timeout)


def getHeight(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getHeight'], timeout=timeout)


def getFee(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getFee'], timeout=timeout)


def getMilestone(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getMilestone'], timeout=timeout)


def getReward(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getReward'], timeout=timeout)


def getSupply(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getSupply'], timeout=timeout)


def getStatus(nodeServer, timeout=4000):
    # TODO: check arguments
    return http.get(nodeServer+_kPaths['getStatus'], timeout=timeout)
