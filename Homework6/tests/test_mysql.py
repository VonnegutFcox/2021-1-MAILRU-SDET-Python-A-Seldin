import re

import pytest

from mysql.builder import MySQLBuilder
from mysql.models import TotalNumberOfRequests, TotalNumberOfRequestsByType,\
    Top10, Top4XX, Top5XX


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()


class TestTotalNumberOfRequests(MySQLBase):
    def prepare(self):
        self.result = sum(1 for line in open('./access.log', 'r'))
        self.mysql_builder.create_total(self.result)

    def get_data(self):
        return self.mysql.session.query(TotalNumberOfRequests).first()

    def test_total_urls(self):
        assert len(self.get_data()) == 1


class TestTotalNumberOfRequestsByType(MySQLBase):
    def prepare(self):
        with open('./access.log', 'r') as file:
            data = [x.split()[5][1:] for x in file]
            result = dict([(x, data.count(x)) for x in set(data)])
        for i in result:
            self.mysql_builder.create_total_by_type(i[0], i[1])

    def get_data(self):
        return self.mysql.session.query(TotalNumberOfRequestsByType).all()


class TestTop10(MySQLBase):
    def prepare(self):
        with open("./access.log", 'r') as f:
            data = [x.split()[6] for x in f]
            sorted_data = sorted([(x, data.count(x)) for x in set(data)],
                                 reverse=True, key=lambda arg: arg[1])[:10]
        for i in sorted_data:
            self.mysql_builder.create_top10(url=i[0],
                                            count_=i[1])

    def get_data(self):
        result = self.mysql.session.query(Top10).all()
        return result

    def test(self):
        result = self.get_data()
        assert len(result) == 10


class Test4XX(MySQLBase):
    def prepare(self):
        with open("./access.log", 'r') as file:
            data = [
                i.split()
                for i in file if re.search(r'4\d\d', i.split()[8])
            ]
            sorted_data = sorted(
                [(i[6], i[8], int(i[9]), i[0]) for i in data],
                key=lambda x: x[2],
                reverse=True)[:5]
        for i in sorted_data:
            self.mysql_builder.create_top4xx(url=i[0],
                                             status_code=i[1],
                                             request_size=i[2],
                                             ip=i[3])

    def get_data(self):
        result = self.mysql.session.query(Top4XX).all()
        return result

    def test(self):
        result = self.get_data()
        assert len(result) == 5


class Test5XX(MySQLBase):
    def prepare(self):
        with open("access.log", 'r') as f:
            data = [x.split() for x in f]
            result = [x[0] for x in data if re.match(r'5\d\d', x[8])]
            sorted_data = sorted([(x, result.count(x)) for x in set(result)],
                                 reverse=True, key=lambda arg: arg[1])[:5]
        for i in sorted_data:
            self.mysql_builder.create_top5xx(ip=i[0],
                                             count_=i[1])

    def get_data(self):
        result = self.mysql.session.query(Top5XX).all()
        return result

    def test(self):
        result = self.get_data()
        assert len(result) == 5
