import sqlalchemy as sa
import datetime
from data.sqlalchemybase import SqlAlchemyBase

class rentals(SqlAlchemyBase):
    __tablename__ = 'rentals'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    start_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)
    end_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

