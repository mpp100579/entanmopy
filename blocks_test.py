#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import blocks

_nodeServer = 'http://39.105.210.35:5000'

if __name__ == "__main__":
    print('getFee', blocks.getFee(_nodeServer))
    print('getHeight', blocks.getHeight(_nodeServer))
    print('getMilestone', blocks.getMilestone(_nodeServer))
    print('getSupply', blocks.getSupply(_nodeServer))
    print('getReward', blocks.getReward(_nodeServer))
    print('getStatus', blocks.getStatus(_nodeServer))
    print('getBlock', blocks.getBlock(_nodeServer, height=2))
    print('getBlock', blocks.getBlock(_nodeServer, blockid='b8f0e9310ede1fc64fbbcdc7dee0edebdd74490017e5b4261573c14c80de591a'))
    print('getFullBlock', blocks.getFullBlock(_nodeServer, height=2))
    print('getFullBlock', blocks.getFullBlock(_nodeServer, blockid='b8f0e9310ede1fc64fbbcdc7dee0edebdd74490017e5b4261573c14c80de591a'))
    print('getBlocks', blocks.getBlocks(_nodeServer, previousBlock='b8f0e9310ede1fc64fbbcdc7dee0edebdd74490017e5b4261573c14c80de591a'))
    print('getBlocks', blocks.getBlocks(_nodeServer, orderBy='height:desc', limit=2))
    print('getBlocks', blocks.getBlocks(_nodeServer, generatorPublicKey='220ca36be9d82e9b88abf25d2bdf8de9fd858f381a3cbd5a01d20a1637f28835', limit=1))