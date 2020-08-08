import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Chipset file convertion: text file read and save to excel file")
    parser.add_argument("--tool", required=True, metavar='convert, rename',
                        choices=['convert', 'rename'],
                        help="convert: convert txt to excel file; rename: bulk rename input file")
    parser.add_argument("--source_dir", required=False, metavar="source-directory/TextFile",
                        help="source directory where output file are present")
    parser.add_argument("--target_dir", required=False, metavar="target-directory/ExcelFile",
                        help="Target directory where excel is to be saved")
    return parser.parse_args()


parse_arguments()
