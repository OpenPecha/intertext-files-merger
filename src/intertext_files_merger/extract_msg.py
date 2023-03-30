import re
import sys

def get_file_names(commit_msg):
    if "merge" in commit_msg.lower():
        input_filenames = re.findall(r'\[([^\]]+)\]', commit_msg)[0].split(', ')
        return input_filenames
    else:
        print("Trigger word 'merge' not found in commit message.")

if __name__=="__main__":
    commit_msg = sys.argv[1]
    #commit_msg= "Merge[files/dmk-t341-t0202-01-padma-20221217.bo.cn.xml, files/dmk-t341-t0202-03-JC-20221217.bo.cn.xml] into [dmk-t341-t0202.bo.cn.xml]"
    input_filenames=get_file_names(commit_msg)
    print(input_filenames)

