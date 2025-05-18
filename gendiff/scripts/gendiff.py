from gendiff.CL_parser import CL_parse
from gendiff.generate_diff import generate_diff


def main():
    params = CL_parse()
    diff = generate_diff(params.first_file, params.second_file, params.format)
    print(diff)


if __name__ == "__main__":
    main()

