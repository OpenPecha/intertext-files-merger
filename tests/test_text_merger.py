from pathlib import Path

expected_output= Path('./tests/data/t001-output/t001.bo.xml').read_text(encoding="utf-8")

def test_merge_text():
    pass
#     files=[]
#     for sublists in regrouped_filenames['t001']['bo']: 
#         files.append(sublists)
    
#     srcs=files[0]
#     dest=files[1]

#     with open(home/baller/work/intertext-files-merger/tests/data/t001-input/srcs,'r') as f:
#         data = f.read() 

#     soup_prev = BeautifulSoup(data,"xml")
#     soup_cur = BeautifulSoup(cur_xml,"xml")
#     print(soup_prev)
      
#     assert merged_test == expected_output


if __name__ == "__main__":
    
    test_merge_text()
