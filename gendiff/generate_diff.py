from gendiff.file_loader import load
from gendiff.formats.format import format


def generate_diff(file_path1, file_path2, format_name='stylish'):
    dict1 = load(file_path1)
    dict2 = load(file_path2)
    diff_tree = recurs_generate_diff(dict1, dict2)
    diff_text = format(diff_tree, format_name)
    return diff_text


def recurs_generate_diff(dict1, dict2):
    diff = {}
    keys = sorted(dict1.keys() | dict2.keys())

    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        
        if isinstance(value1, dict) and isinstance(value2, dict):
            diff[key] = {
                'child':  recurs_generate_diff(value1, value2)
            }
        elif value1 is None:
            diff[key] = [{
                'sign': '+',
                'value': value2
            }]
        elif value2 is None:
            diff[key] = [{
                'sign': '-',
                'value': value1
            }]        
        elif value1 == value2:
            diff[key] = [{
                'sign': ' ',
                'value': value1
            }] 
        else:
            diff[key] = [
            {
               'sign': '-',
               'value': value1
            },
            {
               'sign': '+',
               'value': value2
            }]
    return diff
