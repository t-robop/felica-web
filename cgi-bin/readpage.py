#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(1, os.path.split(sys.path[0])[0])

import nfc
import datetime
import re
from string import Template


def on_startup(targets):
    print ("started!")
    return targets


def on_connect(tag):
    if tag.ndef:
        print tag.ndef.message.pretty()

clf = nfc.ContactlessFrontend('usb')

def print_html(data):
    now = datetime.datetime.now()  # 時刻取得
    visited_booth = []  # 訪れたブースの記号リスト
    booths = ""

    f = open("index.html")  # 表示する雛形html
    html = f.read()
    f.close()

    fs = open("boothdata.txt")  # ブースの記号一覧
    for line in fs:
        line = line.rstrip()
        if line in data:
            visited_booth.append(line)  # タグに記号があったらリストに追加

    fs.close()

    time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
    counttxt = str(len(visited_booth))
    for symbol in visited_booth:
        booths += ("<li class='list-group-item'>" + str(symbol) + "</li>")

    temp = Template(html)  # htmlに代入
    d = {
        'time': time,
        'count': counttxt,
        'visited': booths,
    }

    print "Content-type: text/html\n"
    print temp.substitute(d)
    # print(visited_booth)


def connected(tag):
    if tag.ndef:
        tagdata = tag.ndef.message.pretty()  # tagを読み込み
        tagdata = re.findall("02en[A-Za-z]*", tagdata)  # テキストだけを抽出
        tagdata = tagdata[0]
        tagdata = tagdata[4:]
        tagdata = str(tagdata)
        print_html(tagdata)


clf.connect(rdwr={'on-connect': connected})

clf.close()
