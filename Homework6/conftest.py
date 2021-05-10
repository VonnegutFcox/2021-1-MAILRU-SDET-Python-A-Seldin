import pytest

from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_PYTHON')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', password='pass', db_name='TEST_PYTHON')
        mysql_client.recreate_db()

        mysql_client.connect()

        mysql_client.create_total_number()
        mysql_client.create_total_number_by_type()
        mysql_client.create_top10()
        mysql_client.create_top4xx()
        mysql_client.create_top5xx()

        mysql_client.connection.close()
