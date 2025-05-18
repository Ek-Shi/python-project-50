from gendiff.formats.json import format_json
from gendiff.formats.plain import format_plain
from gendiff.formats.stylish import format_stylish


def format(diff, formatter):
    match formatter:
        case 'stylish':
            return format_stylish(diff)
        case 'plain':
            return format_plain(diff)
        case 'json':
            return format_json(diff)
        case _:
            raise ValueError(f"Wrong formatter: {formatter}")
