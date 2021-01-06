#!/bin/env python3

import argparse
import os
import ftfy # https://ftfy.readthedocs.io/en/latest/


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("path")
    
    args = argument_parser.parse_args()
    print(args.path)

    if not os.path.exists(args.path):
        raise(Exception("The path does not exist: {}".format(args.path)))

    # Rename
    files_list = [os.path.join(args.path, filename) for filename in os.listdir(args.path)]
    for file_name in files_list:

        old_name = file_name
        new_name = ftfy.fix_text(file_name)
        msg = "{}\t-> \t{}".format(old_name, new_name)
        print(msg)
        os.rename(old_name, new_name)

if __name__ == "__main__":
    main()