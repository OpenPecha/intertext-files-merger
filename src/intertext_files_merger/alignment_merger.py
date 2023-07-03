import re
from bs4 import BeautifulSoup

def merge_text(soup,last_xtarget):
    cur_links = soup.find_all("link")
    for cur_link in cur_links:
        xtargets = cur_link["xtargets"].split(";")
        new_xtargets = []
        
        if xtargets[0]!="":
            part1_xtarget= xtargets[0].split(":")
            part1_xtarget[0] = str(int(part1_xtarget[0]) + last_xtarget[0])
        else:
            part1_xtarget=[]
        if xtargets[1]!="":
            part2_xtarget = xtargets[1].split(":")
            part2_xtarget[0] = str(int(part2_xtarget[0]) + last_xtarget[1])
        else:
            part2_xtarget=[]
        new_xtargets.append(":".join(part1_xtarget))
        new_xtargets.append(":".join(part2_xtarget))
        cur_link["xtargets"] = ";".join(new_xtargets)
        cur_link["status"]= cur_link["status"]       

def get_alignment_text(file_paths):
    file_path=file_paths[0]
    file_name=file_path.stem
    extr=re.match("^(\w+-\w+-\w+)(-\w+-\w+-\w+)\.(.*)$",file_name)
    main_file=extr.group(1)
    langs=extr.group(3)
    sep_langs=langs.split(".")
    lang_1=sep_langs[0]
    lang_2=sep_langs[1]
    root_toDoc=f"{main_file}.{lang_2}.xml"
    root_fromDoc=f"{main_file}.{lang_1}.xml"
    new_xml = BeautifulSoup(features='xml')
    root = new_xml.new_tag('linkGrp')
    root['toDoc']=root_toDoc
    root['fromDoc']=root_fromDoc
    new_xml.append(root)
    last_xtarget=[0,0]
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            xml = f.read()
            soup = BeautifulSoup(xml, 'xml')
        l_xtarget=get_last_xtarget(soup)
        second_l_xtarget=second_lxtarget(soup)
        merge_text(soup,last_xtarget)
        create_xml(soup,root)
        update_last_target(last_xtarget,l_xtarget,second_l_xtarget)
    return new_xml.prettify()

def get_last_xtarget(soup):
    cur_file_last_xtarget=soup.find_all('link')[-1]
    xtargets = cur_file_last_xtarget["xtargets"].split(";")
    last_x_target=[]
    for xtarget in xtargets:
        parts = xtarget.split(":")
        last_x_target.append(parts[0])
    return last_x_target

def second_lxtarget(soup):
    link_elements = soup.find_all('link')
    for link in reversed(link_elements):
        xtargets = link.get("xtargets")
        second_last_x_target = []
        parts = xtargets.split(";")
        for i in range(len(parts) - 1):
            current_target = parts[i].split(":")
            next_target = parts[i + 1].split(":")
            if current_target[0] and next_target[0]:
                second_last_x_target.extend([current_target[0], next_target[0]])
                return second_last_x_target
            else:
                break

def create_xml(soup,root):
    link_tags=soup.find_all('link')
    for link_tag in link_tags:
        root.append(link_tag)

def update_last_target(last_xtarget,l_xtarget,second_l_xtarget):
    for i in range(len(last_xtarget)):
        if l_xtarget[i] != '':
            last_xtarget[i] += int(l_xtarget[i])
        else:
            last_xtarget[i]+= int(second_l_xtarget[i])

    return last_xtarget

def merge_alignment_file(alignment_filepaths):
    merged_xmls=get_alignment_text(alignment_filepaths)
    return merged_xmls