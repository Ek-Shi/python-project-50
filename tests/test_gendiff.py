import pytest
import os
from gendiff.scripts.generate_diff import generate_diff


def get_full_path(file_name):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'test_data', file_name)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, expected_file, formatter", [
    ("input/plain/json/file1.json", "input/plain/json/file2.json", 
        "output/plain/stylish.txt", "stylish"),
    ("input/plain/yaml/file1.yaml", "input/plain/yaml/file2.yaml", 
        "output/plain/stylish.txt", "stylish"),
    ("input/tree/json/file1.json", "input/tree/json/file2.json", 
        "output/tree/stylish.txt", "stylish"),
    ("input/tree/yaml/file1.yaml", "input/tree/yaml/file2.yaml", 
        "output/tree/stylish.txt", "stylish"),
    ("input/tree/json/file1.json", "input/tree/json/file2.json", 
        "output/tree/plain.txt", "plain"),
    ("input/tree/yaml/file1.yaml", "input/tree/yaml/file2.yaml", 
        "output/tree/plain.txt", "plain"),
    ("input/tree/json/file1.json", "input/tree/json/file2.json", 
        "output/tree/json.txt", "json"),
    ("input/tree/yaml/file1.yaml", "input/tree/yaml/file2.yaml", 
        "output/tree/json.txt", "json"), 
    ("input/plain/json/file1.json", "input/plain/json/file2.json", 
        "output/plain/stylish.txt", "plain"),
    ("input/plain/yaml/file1.yaml", "input/plain/yaml/file2.yaml", 
        "output/plain/stylish.txt", "json"),
])
def test_generate_diff(file1, file2, expected_file, formatter):
    file1_path = get_full_path(file1)
    file2_path = get_full_path(file2)
    expected_result = read_file(get_full_path(expected_file))
    result = generate_diff(file1_path, file2_path, formatter)
    assert result == expected_result, (
        f"Wrong output with {file1_path} and "
        f"{file2_path}\nexpected\n{expected_result}\ngot\n{result}" 
    )
