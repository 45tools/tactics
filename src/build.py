#!/usr/bin/env python3
"""Build both editions from src/app.html.
   ../index.html          45 Tactics (football only, unchanged look)  -> https://45tools.github.io/tactics/
   ../multi/index.html    45 Tactics Multi (all sports)                -> https://45tools.github.io/tactics/multi/
   ../multi/<sport>/      entry pages that open Multi with that sport selected
"""
import pathlib, re, json, sys
D = pathlib.Path(__file__).parent
ROOT = D.parent
src = (D / 'app.html').read_text()
assert "const EDITION='multi';" in src

# ---- 45 Tactics (football) ----
soccer = src.replace("const EDITION='multi';", "const EDITION='soccer';", 1)
(ROOT / 'index.html').write_text(soccer)

# ---- 45 Tactics Multi ----
MULTI_GUIDE = 'https://note.com/45tools'   # replace with the Multi article URL once it is published
m = src
m = re.sub(r"const GUIDE_URL='[^']*';", f"const GUIDE_URL='{MULTI_GUIDE}';", m, count=1)
m = m.replace('<meta name="apple-mobile-web-app-title" content="45 Tactics">', '<meta name="apple-mobile-web-app-title" content="45 Multi">', 1)
m = m.replace('<title>45 Tactics</title>', '<title>45 Tactics Multi｜スポーツ作戦ボード</title>\n<meta name="description" content="サッカー・バスケ・バレー・野球・ドッジボールなど14競技に対応した、無料・広告なしの作戦ボード。インストール不要、印刷して配布もできます。">', 1)
m = re.sub(r'<link rel="apple-touch-icon" href="data:image/png;base64,[^"]*">', '<link rel="apple-touch-icon" href="icon-180.png">', m, count=1)
out = ROOT / 'multi'
out.mkdir(exist_ok=True)
(out / 'index.html').write_text(m)
(out / 'manifest.webmanifest').write_text(json.dumps({
  "name": "45 Tactics Multi", "short_name": "45 Multi",
  "description": "Free, ad-free tactics board for 14 sports",
  "start_url": "./", "scope": "./", "display": "standalone",
  "background_color": "#E9EFEA", "theme_color": "#E9EFEA",
  "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
            {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=1))

# ---- per-sport entry pages ----
NAMES = {'soccer':'サッカー（11人制）','soccer8':'サッカー（8人制）','futsal':'フットサル','basketball':'バスケットボール','minibasket':'ミニバスケットボール',
         'volley6':'バレーボール（6人制）','volley9':'バレーボール（9人制）','handball':'ハンドボール','dodgeball':'ドッジボール','baseball':'野球',
         'youthbaseball':'学童野球','softball':'ソフトボール','tagrugby':'タグラグビー','hockey':'ホッケー'}
for sid, name in NAMES.items():
    d = out / sid; d.mkdir(exist_ok=True)
    url = f'../?sport={sid}'
    (d / 'index.html').write_text(f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name}の作戦ボード｜45 Tactics Multi（無料・広告なし）</title>
<meta name="description" content="{name}の作戦ボード。無料・広告なし・インストール不要。iPhone・iPad・Android・パソコンのブラウザで使え、印刷して配布もできます。">
<meta http-equiv="refresh" content="0;url={url}"><script>location.replace('{url}')</script></head>
<body><p><a href="{url}">{name}の作戦ボード（45 Tactics Multi）を開く</a></p></body></html>
''')
print('built: index.html', len(soccer), '/ multi/index.html', len(m), '/ entries', len(NAMES))
