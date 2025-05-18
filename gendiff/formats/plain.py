import json


def format_plain(diff):
    return json.dumps(diff, indent=2)
