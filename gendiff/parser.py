from json import loads

from yaml import safe_load


def parse(data, ext):
    match ext:
        case 'json':
            return loads(data)
        case 'yml' | 'yaml':
            return safe_load(data)
        case _:
            raise ValueError(f"Unsupported data format{ext}")
