from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TotalNumberOfRequests(Base):
    __tablename__ = 'total-number-of-request'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TotalNumberOfRequests(" \
               f"id='{self.id}'," \
               f"total='{self.total_number}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    total_number = Column(String(50), nullable=False)


class TotalNumberOfRequestsByType(Base):
    __tablename__ = 'total-number-of-request-by-type'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<TotalNumberOfRequestsByType(" \
               f"id='{self.id}'," \
               f"type='{self.type}', " \
               f"count='{self.count_}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(7), nullable=False)
    count_ = Column(Integer, nullable=False)


class Top10(Base):
    __tablename__ = 'top10'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Top10(" \
               f"id='{self.id}'," \
               f"url='{self.url}', " \
               f"count='{self.count_}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(50), nullable=False)
    count_ = Column(Integer, nullable=False)


class Top4XX(Base):
    __tablename__ = 'top4xx'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Top4XX(" \
               f"id='{self.id}'," \
               f"url='{self.url}', " \
               f"status_code='{self.status_code}', " \
               f"request_size='{self.request_size}', " \
               f"ip='{self.ip}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    status_code = Column(Integer, nullable=False)
    request_size = Column(String(50), nullable=False)
    ip = Column(String(16), nullable=False)


class Top5XX(Base):
    __tablename__ = 'top5xx'
    __table_args__ = {'mysql_charset': 'utf8'}

    def __repr__(self):
        return f"<Top5XX(" \
               f"id='{self.id}'," \
               f"IP='{self.ip}', " \
               f"count='{self.count_}', " \
               f")>"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(16), nullable=False)
    count_ = Column(Integer, nullable=False)
