from modules.cmd_parser import parse_arguments
from modules.file_converter import bulk_file_rename, convert_file

if __name__ == "__main__":
    args = parse_arguments()

    if args.tool == 'convert':
        convert_file(args)
    elif args.tool == 'rename':
        bulk_file_rename(args)
    else:
        exit(1)
