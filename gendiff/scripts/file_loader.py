import os

from gendiff.formats.parser import parse


def load(file):
    ext = get_ext(file)
    with open(file) as f:
        data = f.read()
        return parse(data, ext)


def get_ext(file):
    _, ext = os.path.splitext(file)
    return ext[1:]

