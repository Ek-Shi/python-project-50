import pytest
from gendiff.scripts.parser_of_cl import parse_cl

def test_parse_cl_default_format(monkeypatch):
    monkeypatch.setattr("sys.argv", ["gendiff", "file1.json", "file2.json"])
    args = parse_cl()
    assert args.first_file == "file1.json"
    assert args.second_file == "file2.json"
    assert args.format == "stylish"

def test_parse_cl_custom_format(monkeypatch):
    monkeypatch.setattr("sys.argv", ["prog", "file1.json", "file2.json", "--format", "plain"])
    args = parse_cl()
    assert args.format == "plain"

def test_parse_cl_missing_args(monkeypatch):
    monkeypatch.setattr("sys.argv", ["prog"])
    with pytest.raises(SystemExit):
        parse_cl()
