# felica-web
Webサーバーを建ててブラウザでNFCを読むやつ

# 使いかた
- パソリを接続する
- - vmだと切れやすいので注意
- server.pyを実行
- Chromeから http://localhost:8000/cgi-bin/readpage.py にアクセス
- 読み込み中にNFCタグをかざす
- 結果とともにページが表示される
- もう１回読むときはリロード
- - index.html を編集して自動リロードできます