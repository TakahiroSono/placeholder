# 動作方法

以下のコマンドにてコンテナのビルドを行う。
```bash
docker compose up -d --build
```

コンテナに入る。
```bash
docker compose exec python3 bash
```

コンテナのマウントしている階層に移動する。
```bash
cd opt/
```

下記コマンドにてプログラムを実行する。
```bash
python paceholder.py NAME=<NAME> AGE=<AGE> HOBBY=<HOBBY>
```

# 実行例
全てのパラメータを指定した場合。
```bash
root@b7e104263867:~/opt# python placeholder.py NAME=太郎 AGE=20 HOBBY=サッカー
こんにちは。私は太郎です。
今年で20になります。趣味はサッカーです。
```

パラメータを参照する場合。
```bash
root@b7e104263867:~/opt# python placeholder.py NAME=太郎%HOBBY%%AGE% AGE=20 HOBBY=サッカー%NAME%
こんにちは。私は太郎サッカー20です。
今年で20になります。趣味はサッカー太郎20です。
```

HOBBY を指定しない。
```bash
root@b7e104263867:~/opt# python placeholder.py NAME=太郎 AGE=20
こんにちは。私は太郎です。
今年で20になります。趣味は無趣味です。
```

対象年齢外。
```bash
root@b7e104263867:~/opt# python placeholder.py NAME=太郎 AGE=17
AGE は18〜65の範囲の整数で入力してください。
```

NAME の文字数超過。
```bash
root@b7e104263867:~/opt# python placeholder.py NAME=0123456789012345678901 AGE=18
NAME は１文字以上２０文字以下で入力してください。
```

何派？
```bash
root@b7e104263867:~/opt# python placeholder.py NAME=太郎 AGE=18 HOBBY=犬と遊ぶ
こんにちは。私は太郎です。
今年で18になります。趣味は※と遊ぶです。
root@b7e104263867:~/opt# python placeholder.py NAME=太郎 AGE=18 HOBBY=猫と遊ぶ
こんにちは。私は太郎です。
今年で18になります。趣味は猫と遊ぶです。
```
