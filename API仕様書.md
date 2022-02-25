# お菓子管理アプリ
- [x] ☆POST /users/duties
- [x] ☆ PUT /users/duties
- [x] ☆ DELETE /users/duties/:order
- [x] GET /users/duties
- [ ] ☆ GET /snacks/purchased
- [ ] ☆ POST /snacks/purchased
- [ ] GET /snacks/today
- [ ] GET /snacks/ranking
- [ ] POST /snacks/evaluate/:snack_id
- [ ] GET /snacks/suggest
- [ ] POST /snacks/suggest
- [ ] POST /snacks/favorite/:snack_id
- [ ] DELETE /snacks/favorite/:snack_id

## ☆ POST /users/duties
当番ユーザーの追加(キュー)

## ☆ PUT /users/duties
当番ユーザーの移動
```
{
    "source": int
    "destination": int
}
```

## ☆ DELETE /users/duties/:order
当番ユーザーの削除

## GET /users/duties
当番のユーザーリスト

## ☆ GET /snacks/purchased
買ったお菓子リスト

## ☆ POST /snacks/purchased
買ったお菓子
```
{
    "name": str
}
```

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
