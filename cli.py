import argparse

import os
import sys

# Create parser
my_parser = argparse.ArgumentParser(description='List the contents of specified folder')

# Add arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list from')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The specified path does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
