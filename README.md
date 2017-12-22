【seichi.csvのデータ構造】

第1カラム：一意のID

第2カラム：アニメの作品名
・シリーズ毎に統合している作品と分割している作品がある

第3カラム：アニメ作品名の五十音
・作品名の先頭3文字分を表す6桁の数値
・1文字を2桁の数字で表現
・1桁目を子音の番号(1～9)、2桁目を母音の番号(1～5)とする
・例：あ→11、に→52、め→74、あにめ→115274
・「わ行」は「ら行(91～95)」に続く（例：ん→98）
・別作品で6桁の数値に重複がある場合は、下1桁を+1または-1する

第4カラム：聖地名

第5カラム：聖地のある都道府県名
・「都」「府」「県」は省略

第6カラム：聖地のある住所
・番地が不明確な場合は付近の番地を記載、または記載なしとする

第7カラム：聖地のある緯度

第8カラム：聖地のある経度
