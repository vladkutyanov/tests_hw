import urllib.request
import json
from unittest.mock import patch, MagicMock
import pytest
import get_year


@patch('urllib.request.urlopen')
def test_url_ymd(mock_urlopen):
    cm = MagicMock()
    cm.read.return_value = json.dumps({'$id': '1', 'currentDateTime': '2020-11-29T1'})
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm
    with urllib.request.urlopen('http://localhost'):
        assert get_year.what_is_year_now() == 2020


@patch('urllib.request.urlopen')
def test_url_dmy(mock_urlopen):
    cm = MagicMock()
    cm.read.return_value = json.dumps({'$id': '1', 'currentDateTime': '29.11.2020'})
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm
    with urllib.request.urlopen('http://localhost'):
        assert get_year.what_is_year_now() == 2020


@patch('urllib.request.urlopen')
def test_url_invalid(mock_urlopen):
    cm = MagicMock()
    cm.read.return_value = json.dumps({'$id': '1', 'currentDateTime': '29-1134-2020'})
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm
    with urllib.request.urlopen('http://localhost'):
        assert get_year.what_is_year_now() == 2020
