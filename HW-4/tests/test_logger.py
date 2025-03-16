import os.path

import pytest
from Logger import Logger

@pytest.fixture(scope="function")

def logger_test():
    file = open('test_logger.txt', 'w')
    path = os.path.realpath('test_logger.txt')
    logger_path = Logger(path)

    yield logger_path
    file.close()
    os.remove(path)

@pytest.mark.parametrize("input_data, expected_result",
                         [
                             ("abcde","abcde"),
                             ("185+654","185+654"),
                             ("","")
                         ])

def test_positive_logger(logger_test, input_data, expected_result):
    logger_test.log(input_data)
    data = logger_test.get_logs()
    output_data = [line.rstrip() for line in data]
    output_str = ""
    for element in output_data:
        output_str += element
    assert output_str == expected_result
