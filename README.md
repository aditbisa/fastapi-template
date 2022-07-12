# REST API Template

A REST API template using:
- [Poetry](https://python-poetry.org/) for environment and package management,
- [FastAPI](https://fastapi.tiangolo.com/) for the framework,
- [SQLAlchemy](https://docs.sqlalchemy.org/) for database ORM,
- [Alembic](https://alembic.sqlalchemy.org/) for database migration,
- [PyTest](https://docs.pytest.org/) for testing,
- [pre-commit](https://pre-commit.com/) with:
    - [Black](https://black.readthedocs.io/) for code formatter,
    - [MyPy](https://mypy.readthedocs.io/) for type checker.


## Geared for shared hosting

Why? it's cheap.

- Using [a2wsgi](https://github.com/abersheeran/a2wsgi) in (./app/main.py) for WSGI/passenger server,
- [Gunicorn](https://gunicorn.org/) for dev server.
