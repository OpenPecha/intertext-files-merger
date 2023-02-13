from pathlib import Path
from filename_regrouper import regroup_filename
from bs4 import BeautifulSoup


def merge_text(regrouped_filenames):
    files=[]
    for sublists in regrouped_filenames['t001']['bo']: 
        files.append(sublists)
    
    srcs=files[0]
    dest=files[1]

    #with open(,'r') as f:
    #data = f.read() 

    soup_prev = BeautifulSoup(data,"xml")
    soup_cur = BeautifulSoup(cur_xml,"xml")
    print(soup_prev)

    return regrouped_filenames
    

if __name__ =="__main__":
   input_dir='/home/baller/work/intertext_merge_xml/test/data/t001-input'
   regrouped_filenames=regroup_filename(input_dir)
   merge_text(regrouped_filenames)
   
   


    

    
