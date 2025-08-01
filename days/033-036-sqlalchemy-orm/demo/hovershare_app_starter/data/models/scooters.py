import sqlalchemy as sa
import datetime

from data.sqlalchemybase import SqlAlchemyBase


class Scooter(SqlAlchemyBase):
    __tablename__ = "scooters"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True) # automatically indexed
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    vin = sa.Column(sa.String, index=True, unique=True)
    model = sa.Column(sa.String, index=True)
    batter_level = sa.Column(ksa.Integer, index=True)