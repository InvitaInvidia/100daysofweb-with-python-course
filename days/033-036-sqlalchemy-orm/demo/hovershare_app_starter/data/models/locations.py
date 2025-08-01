import sqlalchemy as sa
import datetime
from data.sqlalchemybase import SqlAlchemyBase

class Locations(SqlAlchemyBase):
    __tablename__ = 'locations'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    street = sa.Column(sa.String)
    city = sa.Column(sa.String, index=True)
    state = sa.Column(sa.String, index=True)

    max_storage = sa.Column(sa.Integer, index=True)
