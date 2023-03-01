from pathlib import Path
from bs4 import BeautifulSoup
from intertext_files_merger.filename_regrouper import regroup_filename

def merge_text(soup, last_p_id):  
    cur_paras = soup.find_all("p")
    for cur_para in cur_paras:
        sentences = cur_para.find_all("s")
        last_p_id+=1
        cur_para.attrs['id'] = last_p_id
        update_sentence(sentences,last_p_id)
        
def update_sentence(sentences,cur_par_id):
    cur_sentence_count =1
    for sentence in sentences:
        sentence.attrs['id'] = f"{cur_par_id}:{cur_sentence_count}"
        cur_sentence_count+=1

def get_language_text(file_paths):
    new_xml = BeautifulSoup(features='xml')
    root = new_xml.new_tag('text')
    new_xml.append(root)
    last_p_id=0
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            xml = f.read()
            soup = BeautifulSoup(xml, 'xml')
        
        cur_file_last_pid=soup.find_all('p')[-1]['id']
        merge_text(soup,last_p_id)
        create_xml(soup,root)
        last_p_id += int(cur_file_last_pid)  
        return new_xml.prettify()

def create_xml(soup,root): 
    p_tags=soup.find_all('p')
    for p_tag in p_tags:
        root.append(p_tag)    
    
def merged_filename(data):
    languages=['bo','cn']
    merged_xmls=[]
    for language in languages:
        if language in languages:
            merged_xml=get_language_text(data[language])
            merged_xmls.append(merged_xml)
        else:
            print(f"Data for {language} language not found.")
    return merged_xmls


def merge_texts(regrouped_filenames): 
    merged_xmls={}
    for file_path,filename_dict in regrouped_filenames.items():
        merged_xml=merged_filename(filename_dict)
        merged_xmls.update({file_path:merged_xml})
    return merged_xmls
    

if __name__ =="__main__":
   input_dir=Path('./tests/data/t001-input')
   regrouped_filenames=regroup_filename(input_dir)
   merge_texts(regrouped_filenames)