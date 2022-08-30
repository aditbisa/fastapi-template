# REST API Template

The first go to develop restfull backend using FastAPI.


# 🛠 The Stack
- [Poetry](https://python-poetry.org/) for environment and package management,
- [FastAPI](https://fastapi.tiangolo.com/) for the framework,
- [SQLAlchemy](https://docs.sqlalchemy.org/) for database ORM,
- [Alembic](https://alembic.sqlalchemy.org/) for database migration,
- [PyTest](https://docs.pytest.org/) for testing,
- [a2wsgi](https://github.com/abersheeran/a2wsgi) for working with WSGI/passenger server,
    - [Gunicorn](https://gunicorn.org/) for dev server,
- [pre-commit](https://pre-commit.com/) with:
    - [Black](https://black.readthedocs.io/) for code formatter,
    - [MyPy](https://mypy.readthedocs.io/) for type checker.


# 📝 TODO
- user auth
  - user model
  - user migration
  - jwt auth
  - login / logout
- user management
  - crud
- docs
- code templates
  - generate with script
- data model to migration script
