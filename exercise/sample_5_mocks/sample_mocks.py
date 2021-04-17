from unittest.mock import Mock, MagicMock

import pytest


class Sample:

    def __init__(self):
        self.sample_str = ...
        self.sample_number = ...

    def some_method(self):
        print('some msg')


def mock1():
    sample = Sample()
    sample.sample_str = 'Ala ma kota'
    sample.some_method()

    mock = Mock()
    mock.sample_str = 'Ala ma kota'
    mock.some_method()


def mock2():
    mock = Mock(return_value='mock_value')  # mock() -> 'mock_value'
    assert mock.return_value == 'mock_value'

    mock.some_method = Mock(
        return_value='mocked_method_value')  # mock.some_method() -> 'mocked_method_value'
    assert mock.some_method() == 'mocked_method_value'

    mock.some_method()
    assert mock.some_method.call_count == 2


def mock3():
    mock = Mock()
    mock.method_with_exception = Mock(side_effect=Exception('some_msg'))
    with pytest.raises(Exception):
        mock.method_with_exception()


def magic_mock1():
    mock = MagicMock()
    mock.sample_str = 'Ala ma kota'
    mock.some_method()


if __name__ == '__main__':
    mock1()
    mock2()
    mock3()
    magic_mock1()
