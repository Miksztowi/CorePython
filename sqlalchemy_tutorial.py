# -*- coding:utf-8 -*-
__author__ = "ganbin"
from distutils.log import warn as printf
from os.path import dirname
from random import randrange as rand
from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base


DBNAME = 'automotive'
DSNs = {
    'mysql': 'mysql://root@localhost/%s' % (DBNAME)
}

Base = declarative_base()
tformat = lambda s : str(s).title().ljust(5, '')
class Users(Base):
    __tablename__ = 'VehicleModelYear'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    make = Column(String)
    model = Column(String)

    def __str__(self):
        return ''.join(
            map(tformat, (self.id, self.year, self.make, self.model))
        )
class SQLAlchemyTest(object):
    def __init__(self, dsn):
        try:
            eng = create_engine(dsn)
        except ImportError:
            raise RuntimeError

        eng.connect()

        Session = orm.sessionmaker(bind=eng)
        self.ses = Session()
        self.users = Users.__table__
        self.eng = self.users.metadata.bind = eng

    def insert(self):
        self.ses.add(
            Users(
                year=2018, make='Binwen', model='Car'
            )
        )
        self.ses.commit()

    def update(self):
        fr = rand(1,50)
        to = rand(1,50)
        i = -1
        users = self.ses.query(
            Users).filter_by(id=fr).all()
        for i,user in enumerate(users):
            user.id = to
        self.ses.commit()
        return fr, to, i+1


    def finish(self):
        self.ses.connection().close()

def main():
    printf("** Connect to %r database" % DBNAME)
    orm = SQLAlchemyTest(DSNs['mysql'])

    
    orm.insert()
    # fr, to ,num = orm.update()
    # print('%d user moved from %d to %d' % (num, fr, to))

if __name__ == '__main__':
    main()

