import pytest
import os
from gendiff import generate_diff


def get_full_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, expected_file, formatter", [
    ("input/plain/json/file1.json", "input/plain/json/file2.json", 
        "output/plain/stylish.txt", "stylish")
])
def test_generate_diff(file1, file2, expected_file, formatter):
    file1_path = get_full_path(file1)
    file2_path = get_full_path(file2)
    expected_result = read_file(get_full_path(expected_file))
    result = generate_diff(file1_path, file2_path, formatter)
    assert result == expected_result, (
        f"Wrong output with {file1_path} and {file2_path}\nexpected\n{expected_result}\ngot\n{result}" 
    )
