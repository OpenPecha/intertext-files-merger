import re
from pathlib import Path


def regroup_filename(input_dir):
    regrouped_filename={}  
    list_of_files=list(input_dir.iterdir())
    list_of_files.sort()

    for file_path in list_of_files:
        try:
            file_name = file_path.stem
            extr=re.match(r"^(\w+-\w+-\w+)(-\d+-\w+-\d+)\.(.*)$",file_name)
            main_file=extr.group(1)
            body = extr.group(2)
            lang=extr.group(3)

            if main_file not in regrouped_filename.keys():
                regrouped_filename[main_file]={}

            if lang not in regrouped_filename[main_file].keys():
                regrouped_filename[main_file][lang]=[]
            regrouped_filename[main_file][lang].append(file_path)
        except:
            print(f'INFO: {file_name} File naming convention not found')

    return regrouped_filename

if __name__ == "__main__":
    input_dir = Path('./tests/data/t001-input')
    regrouped_filename = regroup_filename(input_dir)
    print(regrouped_filename)