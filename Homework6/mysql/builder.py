from faker import Faker

from mysql.models import TotalNumberOfRequests, TotalNumberOfRequestsByType,\
    Top10, Top4XX, Top5XX

fake = Faker()


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_total(self, total_number):
        total = TotalNumberOfRequests(
            total_number=total_number
        )
        self.client.session.add(total)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return total

    def create_total_by_type(self, type_, count_):
        total_by_type = TotalNumberOfRequestsByType(
            type=type_,
            count_=count_
        )
        self.client.session.add(total_by_type)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return total_by_type

    def create_top10(self, url, count_):
        top10 = Top10(
            url=url,
            count_=count_,
        )
        self.client.session.add(top10)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return top10

    def create_top4xx(self, url, status_code, request_size, ip):
        top4xx = Top4XX(
            url=url,
            status_code=status_code,
            request_size=request_size,
            ip=ip
        )
        self.client.session.add(top4xx)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return top4xx

    def create_top5xx(self, ip, count_):
        top5xx = Top5XX(
            ip=ip,
            count_=count_,
        )
        self.client.session.add(top5xx)
        self.client.session.commit()  # no need if sessionmaker autocommit=True
        return top5xx
