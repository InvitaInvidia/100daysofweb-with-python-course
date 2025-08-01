import sqlalchemy as sa
import datetime
from data.sqlalchemybase import SqlAlchemyBase

class users(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, index=True, nullable=True)
    email = sa.Column(sa.String, index=True, nullable=True)
    hased_password = sa.Column(sa.String, index=True, nullable=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    last_login = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    
