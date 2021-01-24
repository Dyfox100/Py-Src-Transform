#!/usr/bin/env python3

import argparse
import os

from pytransformation import File_Transformer
from pytransformation import Transformations


def main(args):
    if not (args.for_2_while or args.name_apps or args.move_var_decls
            or args.all):
        raise ValueError('At least one transformation must be supplied!')
    in_path = args.input_file_or_dir_path
    out_path = args.output_file_or_dir_path
    if out_path == in_path:
        print('Warning in and out paths are the same. Input will be '
              + 'overwritten! Continue? y/n')
        user_input = input().lower().strip()
        while user_input != 'y' and user_input != 'n':
            print('Input Not Understood. Continue? y/n')
            user_input = input.lower().strip()
        if user_input == 'n':
            print('Exiting!')
            return

    input_is_file = (in_path[-3:] == '.py') and (os.path.isfile(in_path))
    output_is_file = (out_path[-3:] == '.py')
    both_files = input_is_file and output_is_file

    input_is_dir = (in_path[-1] == os.sep) and (os.path.isdir(in_path))
    output_is_dir = (out_path[-1] == os.sep)
    both_dirs = input_is_dir and output_is_dir

    if input_is_file != output_is_file or input_is_dir != output_is_dir:
        # mismatched directory and file
        raise ValueError('Both input and output must either be file or '
                         + 'directory path. Ensure file paths end in .py '
                         + 'and directory paths end in the path seperator.')
    if not (both_dirs or both_files):
        # unknown or not found types
        raise ValueError('Input or Output types not recognized. Ensure file '
                         + 'paths end in .py and directory paths end in the '
                         + 'path seperator, and file paths are valid.')
    transformations = []
    if args.for_2_while or args.all:
        transformations.append(Transformations.MAKE_FOR_LOOPS_WHILE)
    if args.name_apps or args.all:
        transformations.append(Transformations.NAME_ALL_FUNCTION_APPLICATIONS)
    if args.move_var_decls or args.all:
        transformations.append(Transformations.MOVE_DECLS_TO_TOP_OF_SCOPE)

    transformer = File_Transformer(transformations)
    if both_files:
        transformer.transform(in_path, out_path)
    elif both_dirs:
        if not os.path.isdir(out_path):
            os.mkdir(out_path)
        in_dir = os.listdir(in_path)

        files = [f for f in in_dir if
                 os.path.isfile(os.path.join(in_path, f)) and f[-3:] == '.py']
        for file in files:
            out_file_path = os.path.join(out_path, file)
            in_file_path = os.path.join(in_path, file)
            transformer.transform(in_file_path, out_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pytransformation provides '
                                     + 'utilities to perform various source '
                                     + 'code transformations that may be '
                                     + 'useful when cross compiling python '
                                     + 'code.')
    parser.add_argument('input_file_or_dir_path', type=str,
                        help='Path of file or directory to transform'
                        + ' code from.')
    parser.add_argument('output_file_or_dir_path', type=str,
                        help='Path of file or directory to output'
                        + ' transformed code.')
    parser.add_argument('-for_2_while', action='store_true',
                        help='If a for to while loop conversion should be'
                        + ' performed.')
    parser.add_argument('-name_apps', action='store_true',
                        help='If all unnamed function applications should be '
                        + ' named.')
    parser.add_argument('-move_var_decls', action='store_true',
                        help='If first variable usage / declaration should'
                        + ' be raised to the top of the scope to have all'
                        + ' variable declarations at top of scope.'
                        + '(Avoids variable hoisting)')
    parser.add_argument('-all', action='store_true',
                        help='If all transformations should be performed')

    args = parser.parse_args()
    main(args)
