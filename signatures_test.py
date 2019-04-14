#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import signatures

_nodeServer = 'http://39.105.210.35:5000'

if __name__ == "__main__":
    print('getFee', signatures.getFee(_nodeServer))