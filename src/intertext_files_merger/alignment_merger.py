from pathlib import Path
from bs4 import BeautifulSoup

def merge_text(soup,last_xtarget):
    cur_links = soup.find_all("link")
    for cur_link in cur_links:
        xtargets = cur_link["xtargets"].split(";")
        new_xtargets = []
        for xtarget in xtargets:
            parts = xtarget.split(":")
            parts[0] = str(int(parts[0]) + last_xtarget[0])

            new_xtargets.append(":".join(parts))
        cur_link["xtargets"] = ";".join(new_xtargets)            

def get_alignment_text(file_paths):
    new_xml = BeautifulSoup(features='xml')
    root = new_xml.new_tag('linkGrp')
    new_xml.append(root)
    last_xtarget=[0,0]
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            xml = f.read()
            soup = BeautifulSoup(xml, 'xml')
        get_last_xtarget(soup)
        merge_text(soup,last_xtarget)
        create_xml(soup,root)
        get_last_xtarget(soup)
        #last_xtarget += int(cur_file_last_xtarget)
        for i in range(len(last_xtarget)):
            last_xtarget[i] += 1
    return new_xml.prettify()

def get_last_xtarget(soup):
    cur_file_last_xtarget=soup.find_all('link')[-1]['xtargets']
    xtargets = cur_file_last_xtarget["xtargets"].split(";")
    last_xtarget=[]
    for xtarget in xtargets:
        parts = xtarget.split(":")
        last_xtarget.append(parts[0])
    return last_xtarget



def create_xml(soup,root):
    link_tags=soup.find_all('link')
    for link_tag in link_tags:
        root.append(link_tag)

def merge_alignment_file(alignment_filepaths):
    merged_xmls=get_alignment_text(alignment_filepaths)
    return merged_xmls
    