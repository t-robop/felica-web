# felica-web

## Description
Webサーバーを建ててブラウザでNFCを読むやつ

## Requirement
### Python version
v2.7.x

### Operating System
- Mac OS X
- Linux

## Setup
### Mac
``` bash
git clone https://github.com/t-robop/felica-web
sudo pip install -U nfcpy
```
``` bash
cd felica-web
python cgi-bin/readpage.py
```

### Linux
``` bash
git clone https://github.com/t-robop/felica-web
sudo pip install -U nfcpy
```
``` bash
cd felica-web
sudo python cgi-bin/readpage.py
```

### How to use
Access to http://localhost:8000/cgi-bin/readpage.py by browser🎉


## License
MIT
