import logging
import os
import shutil
import sys

import allure

from ui.fixtures import *


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}


# def pytest_configure(config):
#     if sys.platform.startswith('win'):
#         base_test_dir = 'C:\\tests'
#     else:
#         base_test_dir = '/tmp/tests'
#
#     if not hasattr(config, 'workerinput'):  # execute only once on main worker
#         if os.path.exists(base_test_dir):
#             shutil.rmtree(base_test_dir)
#         os.makedirs(base_test_dir)
#
#     # save to config for all workers
#     config.base_test_dir = base_test_dir
#
#
# @pytest.fixture(scope='function')
# def test_dir(request):
#     test_name = request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_')
#     test_dir = os.path.join(request.config.base_test_dir, test_name)
#     os.makedirs(test_dir)
#     return
#
#
# @pytest.fixture(scope='function', autouse=True)
# def logger(test_dir, config):
#     log_formatter = logging.Formatter('%(asctime)s - %(filename)-15s - %(levelname)-6s - %(message)s')
#     log_file = os.path.join(test_dir, 'test.log')
#
#     log_level = logging.DEBUG if config['debug_log'] else logging.INFO
#
#     file_handler = logging.FileHandler(log_file, 'w')
#     file_handler.setFormatter(log_formatter)
#     file_handler.setLevel(log_level)
#
#     log = logging.getLogger('test')
#     log.propagate = False
#     log.setLevel(log_level)
#     log.handlers.clear()
#     log.addHandler(file_handler)
#
#     yield log
#
#     for handler in log.handlers:
#         handler.close()
#
#     with open(log_file, 'r') as f:
#         allure.attach(f.read(), 'test.log', attachment_type=allure.attachment_type.TEXT)
