# give_me_snack
## 開発の手順
1. `git clone <リポジトリのURL>`でクローンします．
1. `cp .env.sample .env`でコピーし，`.env`を編集します．
1. `docker-compose up -d --build`でビルドしつつコンテナを立ち上げます．(2回目以降は`--build`はいらない)
1. `localhost:8000`にアクセスしてSwaggerUIからAPIサーバーを触りながら開発してください．

## 止め方
1. `docker-compose down`で止めます．  
DBのリレーションを編集したため削除したい場合は`--volumes`をつけるとリレーションもまとめて消すことが出来ます．

## Adminerの使い方
1. Adminerのコンテナを起動していないときは`docker-compose up -d adminer`で起動してください．
1. `localhost:8080`にアクセスして，`.env`で設定したユーザーとパスワードでPostgreSQLにログインします．
1. データベースをGUIで操作できます．詳細は各自調べてください．
