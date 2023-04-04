from pathlib import Path
from intertext_files_merger.filename_regrouper import regroup_filename


def test_regroup_filename():
    input_dir = Path('./tests/data/t001-input')
    expected_output = {
        "dmk-t341-t0202":{
            'bo': [
            Path("./tests/data/t001-input/dmk-t341-t0202-10-padma-20221217.bo.xml"),
            Path("./tests/data/t001-input/dmk-t341-t0202-11-JC-20221210.bo.xml")
            ],
            'cn': [
            Path("./tests/data/t001-input/dmk-t341-t0202-10-padma-20221217.cn.xml"),
            Path("./tests/data/t001-input/dmk-t341-t0202-11-JC-20221210.cn.xml")
            ],
            'bo.cn': [
            Path("./tests/data/t001-input/dmk-t341-t0202-10-padma-20221217.bo.cn.xml"),
            Path("./tests/data/t001-input/dmk-t341-t0202-11-JC-20221210.bo.cn.xml")
            ]
        }   
    }
    
    regrouped_filename = regroup_filename(input_dir)
    assert regrouped_filename == expected_output

if __name__ == "__main__":
    test_regroup_filename()
