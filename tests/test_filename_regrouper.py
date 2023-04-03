from pathlib import Path
from intertext_files_merger.filename_regrouper import regroup_filename


def test_regroup_filename():
    expected_output = {
        "dmk-t341-t0202":{
            'bo': [
            Path("./data/input/dmk-t341-t0202-01-padma-20221217.bo.xml"),
            Path("./data/input/dmk-t341-t0202-03-JC-20221217.bo.xml")
            ],
            'cn': [
            Path("./data/input/dmk-t341-t0202-01-padma-20221217.cn.xml"),
            Path("./data/input/dmk-t341-t0202-03-JC-20221217.cn.xml")
            ],
            'bo.cn': [
            Path("./data/input/dmk-t341-t0202-01-padma-20221217.bo.cn.xml"),
            Path("./data/input/dmk-t341-t0202-03-JC-20221217.bo.cn.xml")
            ]
        }   
    }
    
    file_name=["dmk-t341-t0202-01-padma-20221217.bo.cn.xml","dmk-t341-t0202-03-JC-20221217.bo.cn.xml"]
    regrouped_filename = regroup_filename(file_name)
    assert regrouped_filename == expected_output

if __name__ == "__main__":
    test_regroup_filename()
