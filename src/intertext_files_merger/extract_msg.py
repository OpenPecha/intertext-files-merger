import re
import sys

def get_file_names(commit_msg):
    if "merge" in commit_msg.lower():
        input_filenames = re.findall(r'\[([^\]]+)\]', commit_msg)[0].split(', ')
        return input_filenames
    else:
        print("Trigger word 'merge' not found in commit message.")

if __name__=="__main__":
    #commit_msg = sys.argv[1]
    commit_msg= "Merge[t001-01-padma.bo.cn.xml, t001-03-jc.bo.cn.xml] into [dmk-t341-t0202.bo.cn.xml]"
    input_filenames=get_file_names(commit_msg)
    print(input_filenames)

