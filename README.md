# Pythonによるwebスクレイピングのテスト

## 概要
wikipediaの今日は何の日の部分のみを取得するだけのプログラム。  
httpリクエストにrequests  
スクレイピングにBeautifulSoup  
が必要なのでそれぞれインストールしておく。
## 使い方
. bf/bin/activate
で仮想環境にしてから
ターミナルでbs4_test01.pyを実行すると今日は何の日がprintされる。
## 追加機能
bs4_userArgnet.pyを実行すると自身のIPやUserAgentを取得できる。
ユーザーエージェントを偽装してあるので、偽装したUAが表示される。