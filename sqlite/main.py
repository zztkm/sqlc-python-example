from db.query_sqlite import Querier

from sqlalchemy import create_engine


def main():
    engine = create_engine("sqlite:///test.db")

    with open("schema_sqlite.sql", mode="r") as r:
        sql = r.read()
        # create table
        try:
            engine.execute(sql)
        except:
            pass
    
    queries = Querier(engine.connect())

    # list all authors
    authors = queries.list_authors()
    for author in authors:
        print(author)

    # create an author
    created = queries.create_author(name="zztkm", bio="a programmer")
    print("created: ", created.id, created.name, created.bio)

    # get the author we just inserted
    author = queries.get_author(id=created.id)

    print(created == author)


if __name__ == "__main__":
    main()