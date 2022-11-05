import os
import argparse
from tqdm import tqdm


def main():
    args = get_args()
    input_path = os.path.expanduser(args.input)
    print(os.listdir(input_path))
    for file in tqdm(os.listdir(input_path)):
        print(input_path + "/" + file, rename(input_path, file))
    print("Hello World!")


def get_args():
    parser = argparse.ArgumentParser(
        prog="Series renamer",
        description="Renames episodes in a series to a standard format",
    )
    parser.add_argument("-i", help="Input folder", required=True, dest="input")
    args = parser.parse_args()

    return args


def rename(parent_directory: str, file: str):
    return parent_directory + "-" + file


if __name__ == "__main__":
    main()
