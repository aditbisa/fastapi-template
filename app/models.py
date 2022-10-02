import sqlalchemy as sa
from argon2 import PasswordHasher

from app.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = sa.Column("id", sa.Integer, primary_key=True, autoincrement=True)
    username = sa.Column("username", sa.String, nullable=False)
    password = sa.Column("password", sa.String, nullable=False)

    @sa.orm.validates("password")
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