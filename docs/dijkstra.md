# ダイクストラでありがちなミス
https://snuke.hatenablog.com/entry/2021/02/22/102734
こちらの記事も参考に。

## 取り出し順序ミス
特に**tupleの順番ミス**で引き起こされやすい。queueの中身は`(score, now)`とし、`(now, score)`とはしないように。
失敗例: /joi/joi2024ho/b/

## スコア不一致時のcontinue忘れ
必ずtupleとしてnow_scoreを持っておき、リストとスコアが一致しないときにはcontinueする。
