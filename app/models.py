from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    # _tablename_ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(32), nullable=False, unique=True)

    # quotas = db.Column(db.Integer, nullable=False)
    # init_quotas = db.Column(db.Integer, nullable=False)

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
