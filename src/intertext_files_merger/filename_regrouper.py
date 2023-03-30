import re
from pathlib import Path
from intertext_files_merger.extract_msg import get_file_names,commit_msg

input_dir = Path('./tests/data/t001-input')

def regroup_filename(input_filenames):  
    regrouped_filename={} 

    for file_name in input_filenames:
        extr=re.match("^([^-]*)([^\.]*)\.(.*)(\.xml)$",file_name)
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

    return regrouped_filename

if __name__ == "__main__":
    #input_filenames=get_file_names(commit_msg)
    input_filenames=["t001-01-padma.bo.cn.xml","t001-03-jc.bo.cn.xml"]
    regrouped_filename = regroup_filename(input_filenames)
    print(regrouped_filename)

    