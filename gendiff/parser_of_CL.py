import argparse


def parse_cl():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, 
        default='stylish', help='set format of output')
    args = parser.parse_args()
    return args

