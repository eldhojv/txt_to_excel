import os
from colorama import init, Fore, Style

TXT_MODE = 'rt'
TXT_FILE_TYPE = 'txt'
XLSX_FILE_TYPE = 'xlsx'
INPUT_FILE_NAME = 'InputFile'
INPUT_FILE_RENAMED = 'InputFileRenamed'

ROOT_DIR = ''
DEFAULT_SOURCE_DIR = os.path.join(ROOT_DIR, 'TextFile')
DEFAULT_TARGET_DIR = os.path.join(ROOT_DIR, 'ExcelFile')

INFO_TXT = Fore.CYAN
CL_RESET = Fore.RESET
INFO = Fore.BLUE+'[INFO] '+Fore.RESET
ERROR = Fore.RED+'[ERROR] '+Fore.RESET
SUCCESS = Fore.GREEN
WARNING = Fore.YELLOW+'[WARNING] '+Fore.RESET

ITEM_STR_START = 'Item'
ITEM_STR_END = ' < COMPONENT INSTANCE >'
REF_DESC_STR_START = 'Reference Designator:'
REF_DESC_STR_END = 'Package Symbol:'
DESCRIPTION_STR_START = 'DESCRIPTION       ='
DESCRIPTION_STR_END = 'DEVICE'
DEVICE_STR_START = 'DEVICE            ='
DEVICE_STR_END = 'GOLDEN_PART'
PIN_IO_INFO = 'Pin IO Information:'

PIN1NET_STR_START = '1'
PIN1NET_STR_END = '2'
PIN2NET_STR_START = '2'
PIN2NET_STR_END = '\n'

LINE_END =   '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
FILE_END = '  ~ ~ ~ ~ ~ ~ ~end-of-file~ ~ ~ ~ ~ ~ ~'
SINGLE_SPACE = ' '
NEWLINE_CHAR = '\s+'

ITEM_TXT = "Item"
REF_TXT = "Reference Designator"
DESC_TXT = "Description"
DEVICE_TXT = "Device"
P1N_TXT = "Pin1 Net"
P2N_TXT = "Pin2 Net"

