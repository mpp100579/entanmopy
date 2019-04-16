#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import signatures

_nodeServer = 'http://39.105.210.35:5000'
_secondSecret='123456'
_genesisSecret = 'fluid bracket forum either face bird toy april boss stamp february pencil'

if __name__ == "__main__":
    print('getFee', signatures.getFee(_nodeServer))
    print('addSignature', signatures.add(_nodeServer,_genesisSecret,_secondSecret))