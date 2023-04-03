import re

def get_file_names(commit_msg):
    if "merge" in commit_msg.lower():
        input_filenames = re.findall(r'\[([^\]]+)\]', commit_msg)[0].split(',')
        return input_filenames
    else:
        print("Trigger word 'merge' not found in commit message.")