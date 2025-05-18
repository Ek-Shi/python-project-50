from gendiff import generate_diff
from gendiff.CL_parser import CL_parse


def main():
    params = CL_parse()
    diff = generate_diff(params.first_file, params.second_file, params.format)
    print(diff)


if __name__ == "__main__":
    main()

