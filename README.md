# Getting started sqlc with Python

sql v1.15.0 時点では Python は PostgreSQL しかサポートされていませんでした。

MySQL と SQLite の場合、コードは生成されますが型は自分でつける必要がありそうです。

サポートについては以下を参照してください。
- https://docs.sqlc.dev/en/latest/reference/language-support.html

## SQL生成

以下を実行するには sqlc のインストールが必要です。
https://docs.sqlc.dev/en/latest/overview/install.html

```shell
# example sqlite
cd sqlite

# コマンドを実行すると db dir が上書きされます
sqlc generate
```

root から見て `sqlite/db` ディレクトリにファイルが生成されているのでそれを確認してください。

## 参考

- https://docs.sqlc.dev/en/latest/index.html
- https://docs.sqlc.dev/en/latest/reference/config.html#python
