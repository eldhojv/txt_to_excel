import os
import re
import string
from modules.const import *
from modules.utils import *
from modules.file_tools import *

def convert_file(args):
    source_dir, target_dir = find_file_path(args)
    for each_file in os.listdir(source_dir):
        file_obj = open(file_path_and_name(source_dir, each_file))
        file_content = file_obj.read()
        datas = file_content.split(LINE_END)
        file_obj.close() 
        excel_file_name = check_excel_file_name(source_dir, target_dir, each_file)
        file_dict = {ITEM_TXT:[],REF_TXT:[],DESC_TXT:[],DEVICE_TXT:[],P1N_TXT:[],P2N_TXT:[]}
        
        for each_data in datas:
            if ITEM_STR_START in each_data:
                item_val = each_data[each_data.find(ITEM_STR_START)+len(ITEM_STR_START):each_data.rfind(ITEM_STR_END)]
                file_dict[ITEM_TXT].append(item_val.strip())
            if REF_DESC_STR_START in each_data:
                ref_value = each_data[each_data.find(REF_DESC_STR_START)+len(REF_DESC_STR_START):each_data.rfind(REF_DESC_STR_END)]
                file_dict[REF_TXT].append(ref_value.strip())
            if DESCRIPTION_STR_START in each_data:
                desc_value = each_data[each_data.find(DESCRIPTION_STR_START)+len(DESCRIPTION_STR_START):each_data.rfind(DESCRIPTION_STR_END)]
                desc_value = re.sub(NEWLINE_CHAR, SINGLE_SPACE, desc_value)
                file_dict[DESC_TXT].append(desc_value.strip())
            if DEVICE_STR_START in each_data:
                dev_value = each_data[each_data.find(DEVICE_STR_START)+len(DEVICE_STR_START):each_data.rfind(DEVICE_STR_END)]
                file_dict[DEVICE_TXT].append(dev_value.strip())
            if PIN_IO_INFO in each_data:
                pin_values = each_data[each_data.find(PIN_IO_INFO):]
                p1n_value, p2n_value = extract_pin_info(pin_values)
                file_dict[P1N_TXT].append(p1n_value.strip())
                file_dict[P2N_TXT].append(p2n_value.replace(FILE_END,SINGLE_SPACE).strip())

        write_to_excel_file(target_dir, excel_file_name, file_dict)         
    return


def extract_pin_info(pin_values):
    p1n_value = pin_values[pin_values.find(PIN1NET_STR_START)+40:pin_values.rfind(PIN1NET_STR_END)]
    p2n_value = pin_values[pin_values.find(PIN2NET_STR_START)+40:]
    return p1n_value, p2n_value

