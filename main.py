import os
import argparse
import re


def main():
    args = get_args()
    input_path = os.path.expanduser(args.input)

    for path, subdirs, files in os.walk(input_path):
        for subdir in subdirs:
            path_to = os.path.join(path, subdir)
            for file in os.listdir(path_to):
                os.rename(
                    os.path.join(path_to, file),
                    os.path.join(path_to, rename(subdir, file, path_to)),
                )


def get_args():
    parser = argparse.ArgumentParser(
        prog="Series renamer",
        description="Renames episodes in a series to a standard format",
    )
    parser.add_argument("-i", help="Input folder", required=True, dest="input")
    args = parser.parse_args()

    return args


def rename(parent_directory: str, file: str, path_to: str):
    if (
        file.__contains__("Season")
        or file.__contains__("season")
        or file.__contains__(parent_directory)
        or re.search("[\w]+-(S\d)?E\d?\d\d.\w+", file)
    ):
        return file

    if parent_directory.__contains__("Season") or parent_directory.__contains__(
        "season"
    ):
        path_items = path_to.split("\\")
        return (
            path_items[-2].replace(" ", "_")
            + "-"
            + path_items[-1]
            .replace("eason", "")
            .replace("s", "S")
            .replace("_", "")
            .replace(" ", "")
            + file
        )

    return parent_directory.replace(" ", "_") + "-" + file


if __name__ == "__main__":
    main()
