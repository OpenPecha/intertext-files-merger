import re
import os
import shutil
from intertext_files_merger.extract_msg import get_file_names,commit_msg

input_directory = "./tests/data/t001-input"
output_dir = "./tests/data/t001_output"

def save_text(input_filenames):
    list_of_filenames=[]
    for file_name in input_filenames:
        extr=re.match(r"^([^-]*)([^\.]*)\.(.*)(\.xml)$",file_name)
        main_file=extr.group(1)
        body=extr.group(2)
        langs=extr.group(3)
        list_of_langs=[]
        sep_langs=langs.split(".")
        list_of_langs.append(langs)
        for lang in sep_langs:
            list_of_langs.append(lang)
        for lang in list_of_langs:
            list_of_filenames.append(f"{main_file}{body}.{lang}.xml")
        split_text_id_name= "split_"+str(main_file)
        for filename in list_of_filenames:
            input_file_path = os.path.join(input_directory,filename)
            split_text_id_dir = os.path.join(output_dir, split_text_id_name)
            output_file_path=  os.path.join(split_text_id_dir, filename)
            if not os.path.exists(split_text_id_dir):
                os.makedirs(split_text_id_dir)
            shutil.copyfile(input_file_path, output_file_path)
            #print(f'Copied file {filename} to {split_text_id_dir}')

if __name__ == "__main__":
    #input_filenames=["t001-01-padma.bo.cn.xml","t001-03-jc.bo.cn.xml"]
    input_filenames=get_file_names(commit_msg)
    save_text(input_filenames)