#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import lockvote

_nodeServer = 'http://39.105.210.35:5000'

_genesisAddress = 'A3Es8Thkr7UWWfn4H1y4v9aJcP89GVpa4W'
_genesisTrId = '289c0738ee485ba6f289f015fd2ae7b632e8c1167c40e5a55d663c32ad05b67d'

if __name__ == "__main__":
    print('getAllLockVotes', lockvote.getAllLockVotes(_nodeServer, _genesisAddress))
    print('getLockVote', lockvote.getLockVote(_nodeServer, _genesisTrId))