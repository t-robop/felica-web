#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(1, os.path.split(sys.path[0])[0])

import nfc
import time
import re

clf = nfc.ContactlessFrontend('usb')

def connected(tag):
    tagdata = tag.ndef.message.pretty()             #tagを読み込み
    tagdata = re.findall("02en[A-Za-z]*", tagdata)  #テキストだけを抽出
    tagdata = tagdata[0]
    tagdata = tagdata[4:]
    print(tagdata)

clf.connect(rdwr={'on-connect': connected})