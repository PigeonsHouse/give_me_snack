# お菓子管理アプリ
## ☆ POST /users/duty
当番ユーザーの追加(キュー)

## ☆ PUT /users/duty
当番ユーザーの移動
```
{
    "source": int
    "destination": int
}
```

## ☆ DELETE /users/duty/:order
当番ユーザーの削除

## ☆ GET /snacks/purchased
買ったお菓子リスト

## ☆ POST /snacks/purchased
買ったお菓子
```
{
    "name": str
}
```

## GET /users/duty
当番のユーザーリスト

## GET /snacks/today
今日のお菓子のリスト

## GET /snacks/ranking
お菓子ランキング(評価)

## POST /snacks/evaluate/:snack_id
お菓子へ評価
```
{
    "point": int
}
```

## GET /snacks/suggest
提案されているお菓子一覧

## POST /snacks/suggest
提案されるお菓子
```
{
    "name": str
}
```

## POST /snacks/favorite/:snack_id
提案されているお菓子にいいね

## DELETE /snacks/favorite/:snack_id
提案されているお菓子のいいね解除
