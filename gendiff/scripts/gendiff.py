from gendiff import generate_diff
from gendiff.scripts.parser_of_cl import parse_cl


def main():
    params = parse_cl()
    diff = generate_diff(params.first_file, params.second_file, params.format)
    print(diff)


if __name__ == "__main__":
    main()

