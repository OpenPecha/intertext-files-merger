import re
from pathlib import Path


input_dir = Path('./data/input')

def regroup_filename(input_filenames):  
    regrouped_filename={} 

    for file_name in input_filenames:
        try:
            extr=re.match("^(\w+-\w+-\w+)(-\w+-\w+-\w+)\.(.*)(\.xml)$",file_name)
            main_file=extr.group(1)
            body=extr.group(2)
            langs=extr.group(3)

            list_of_langs=[]
            sep_langs=langs.split(".")
            list_of_langs.append(langs)
            for lang in sep_langs:
                list_of_langs.append(lang)

            for lang in list_of_langs:
                if main_file not in regrouped_filename.keys():
                    regrouped_filename[main_file]={}

                if lang not in regrouped_filename[main_file].keys():
                    regrouped_filename[main_file][lang]=[]
                filename=f"{main_file}{body}.{lang}.xml"
                file_path=Path(input_dir)/filename
                regrouped_filename[main_file][lang].append(file_path)
        except:
            print(f'INFO: {file_name} file naming convention not found')

    return regrouped_filename
