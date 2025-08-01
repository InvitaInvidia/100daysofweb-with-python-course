import sqlalchemy
import sqlalchemy as sa
import sqlalchemy.orm as orm

__engine = None
__factory = None


def global_init(db_name:str):
    global __engine, __factory

    if __factory:
        return

    conn_str = 'sqlite:///' + db_folder.get_full_path(db_name) + '.db'
    __engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=__engine)

def create_tables():
    pass

def create_session()-> sqlalchemy.orm.Session:
    pass