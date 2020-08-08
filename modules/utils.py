import os
import random
import fnmatch
from datetime import date
from modules.const import *

init(autoreset = True)

def find_file_path(args):
    if not args.source_dir:
        source_file_directory = DEFAULT_SOURCE_DIR
    else:
        source_file_directory = args.source_dir

    if not os.path.exists(source_file_directory):
        print(Fore.RED+"Source file directory not found")
        exit(1)

    if not args.target_dir:
        target_file_directory = DEFAULT_TARGET_DIR
    else:
        target_file_directory = os.path.join(args.target_dir, 'ExcelFile')

    if not os.path.exists(target_file_directory):
        os.makedirs(target_file_directory)

    return source_file_directory, target_file_directory


def today_date():
    return date.today().strftime('%Y%m%d')

def file_count(directory):
    return len(fnmatch.filter(os.listdir(directory), '*.'+TXT_FILE_TYPE))

def new_file_name(directory, count):
    return directory+'/'+INPUT_FILE_NAME+str(count)+' - '+today_date()+'.'+TXT_FILE_TYPE

def file_path_and_name(directory, file_name):
    return directory+'/'+file_name

