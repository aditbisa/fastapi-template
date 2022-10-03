import sqlalchemy as sa
from argon2 import PasswordHasher
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

# Mypy will complain variables-vs-type-aliases when use Base as class.
# https://github.com/sqlalchemy/sqlalchemy2-stubs/issues/54
Base = declarative_base()


class UserModel(Base):  # type: ignore
    __tablename__ = "users"

    id = sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True)
    username = sa.Column("username", sa.String(50), nullable=False)
    password = sa.Column("password", sa.String(255), nullable=False)

    @validates("password")
    def _validate_password(self, key, password):
        """
        Hash password using Argon2 as soon as it is assigned.
        """
        ph = PasswordHasher()
        return ph.hash(password)

    def verify_password(self, password) -> int:
        """
        Verify password and return an integer:
        0: for fail,
        1: for sucess and no rehash,
        2: for success with rehash and need session commit.

        Rehash is needed when the Argon2 parameter is changed.
        """
        try:
            ph = PasswordHasher()
            ok = ph.verify(self.password, password)

            if ok and ph.check_needs_rehash(hash):
                self.password = password
                return 2

            return 1
        except Exception:
            pass

        return 0
