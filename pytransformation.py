import argparse
# import os
#
# from pytransformation import File_Transformer
# from pytransformation import Transformations


def main(args):
    if not (args.for2while or args.nameApps or args.moveVarDecls or args.all):
        raise ValueError("At least one transformation must be supplied!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Pytransform')
    parser.add_argument('Input File / Directory Path', type=str,
                        help='Path of file or directory to transform'
                        + ' code from')
    parser.add_argument('Output File / Directory Path', type=str,
                        help='Path of file or directory to output'
                        + ' transformed code.')
    parser.add_argument('--for2while', nargs='?',
                        help='If a for to while loop conversion should be'
                        + ' performed.')
    parser.add_argument('--nameApps', nargs='?',
                        help='If all unnamed function applications should be '
                        + ' named.')
    parser.add_argument('--moveVarDecls', nargs='?',
                        help='If first variable usage / declaration should'
                        + ' be raised to the top of the scope to have all'
                        + ' variable declarations at top of scope.'
                        + '(Avoids variable hoisting)')
    parser.add_argument('--all', nargs='?',
                        help='If all transformations should be performed')

    args = parser.parse_args()
    main(args)
