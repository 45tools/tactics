# 45 Tactics / 45 Tactics Multi のソース

- 元ファイルは `src/app.html` の1つだけ。**直すのはここ**。
- `python3 src/build.py` で次の2つを書き出す（どちらも直接は編集しない）
  - `index.html` … 45 Tactics（サッカー専用、https://45tools.github.io/tactics/）
  - `multi/index.html` … 45 Tactics Multi（14競技、https://45tools.github.io/tactics/multi/）
  - `multi/<競技>/index.html` … 競技ごとの入口（例 `/multi/basketball/`）
- 競技の定義は app.html の `SPORTS`（コートの寸法・人数・並び方・ポジション）と `draw〇〇()`（コートの線）。
- Multiの使い方記事ができたら build.py の `MULTI_GUIDE` を記事URLにする。
