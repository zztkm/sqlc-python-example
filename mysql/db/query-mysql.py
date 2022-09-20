# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.15.0
# source: query-mysql.sql
from typing import Any, Iterator, Optional

import sqlalchemy

from db import models


CREATE_AUTHOR = """-- name: create_author \\:execresult
INSERT INTO authors (
  name, bio
) VALUES (
  ?, ?
)
"""


DELETE_AUTHOR = """-- name: delete_author \\:exec
DELETE FROM authors
WHERE id = ?
"""


GET_AUTHOR = """-- name: get_author \\:one
SELECT id, name, bio FROM authors
WHERE id = ? LIMIT 1
"""


LIST_AUTHORS = """-- name: list_authors \\:many
SELECT id, name, bio FROM authors
ORDER BY name
"""


UPDATE_AUTHOR = """-- name: update_author \\:exec
UPDATE authors
set name = ?,
bio = ?
WHERE id = ?
"""


class Querier:
    def __init__(self, conn: sqlalchemy.engine.Connection):
        self._conn = conn

    def create_author(self, *, name: Any, bio: Optional[Any]) -> sqlalchemy.engine.Result:
        return self._conn.execute(sqlalchemy.text(CREATE_AUTHOR), {"p1": name, "p2": bio})

    def delete_author(self, *, id: Any) -> None:
        self._conn.execute(sqlalchemy.text(DELETE_AUTHOR), {"p1": id})

    def get_author(self, *, id: Any) -> Optional[models.Author]:
        row = self._conn.execute(sqlalchemy.text(GET_AUTHOR), {"p1": id}).first()
        if row is None:
            return None
        return models.Author(
            id=row[0],
            name=row[1],
            bio=row[2],
        )

    def list_authors(self) -> Iterator[models.Author]:
        result = self._conn.execute(sqlalchemy.text(LIST_AUTHORS))
        for row in result:
            yield models.Author(
                id=row[0],
                name=row[1],
                bio=row[2],
            )

    def update_author(self, *, name: Any, bio: Optional[Any], id: Any) -> None:
        self._conn.execute(sqlalchemy.text(UPDATE_AUTHOR), {"p1": name, "p2": bio, "p3": id})