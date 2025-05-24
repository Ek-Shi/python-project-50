from gendiff import generate_diff
from gendiff.parser_of_CL import parse_cl


def main():
    params = parse_cl()
    diff = generate_diff(params.first_file, params.second_file, params.format)
    print(diff)


if __name__ == "__main__":
    main()

