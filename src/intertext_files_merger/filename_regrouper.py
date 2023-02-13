import os
import re


def regroup_filename(input_dir):
    regrouped_filename={}  
    list_of_files=os.listdir(input_dir)

    for file_name in list_of_files:
        extr=re.match(r"^([^-]*)[^\.]*\.(.*)(\.xml)$",file_name)
        main_file=extr.group(1)
        lang=extr.group(2)

        if main_file not in regrouped_filename.keys():
            regrouped_filename[main_file]={}

        if lang not in regrouped_filename[main_file].keys():
            regrouped_filename[main_file][lang]=[]
        regrouped_filename[main_file][lang].append(file_name)

    return regrouped_filename

if __name__ == "__main__":
    input_dir = '/home/baller/work/intertext-files-merger/tests/data/t001-input'
    regrouped_filename = regroup_filename(input_dir)
    print(regrouped_filename)