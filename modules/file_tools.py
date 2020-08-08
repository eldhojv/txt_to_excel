import xlsxwriter
from modules.const import *
from modules.utils import *


def bulk_file_rename(args):
    source_dir, _ = find_file_path(args)
    for index, file in enumerate(os.listdir(source_dir)):
        if file.endswith(TXT_FILE_TYPE):
            os.rename(file_path_and_name(source_dir, file),
                      new_file_name(source_dir, index))
    print(INFO+"Bluk File rename complete")
    return

def rename_file(source_dir, file_name):
    rn_file = INPUT_FILE_RENAMED+str(random.randint(0,file_count(source_dir)))+" - "+today_date()+'.'+TXT_FILE_TYPE
    os.rename(file_path_and_name(source_dir, file_name), file_path_and_name(source_dir, rn_file))
    return rn_file

def check_excel_file_name(source_dir, target_dir, file_name):
    if os.path.exists(file_path_and_name(target_dir,file_name.split(".")[0])+"."+XLSX_FILE_TYPE):
        print(WARNING+"Excel file name already exits")
        print(INFO+"Renaming source directory file")
        rn_file = rename_file(source_dir, file_name)
        print(INFO+"Source directory File name "+INFO_TXT+file_name+CL_RESET+" changed to "+INFO_TXT+rn_file+CL_RESET)
        file_name = rn_file
    return file_name.split(".")[0]+"."+XLSX_FILE_TYPE

def write_to_excel_file(target_dir, excel_file_name, file_dict):
    row = col = 0
    work_book = xlsxwriter.Workbook(file_path_and_name(target_dir, excel_file_name))
    bold = work_book.add_format({'bold': True})
    work_sheet = work_book.add_worksheet() 
    for each_key in file_dict.keys():
        row = 0
        work_sheet.write(row, col, each_key, bold)
        for each_item in file_dict[each_key]:
            row+=1
            work_sheet.write(row, col, each_item)
        col+= 1
    work_book.close()
    print(INFO+"Conversion of "+INFO_TXT+excel_file_name.split(".")[0]+"."+TXT_FILE_TYPE+CL_RESET+" to excel file "+SUCCESS+" completed")
    return

