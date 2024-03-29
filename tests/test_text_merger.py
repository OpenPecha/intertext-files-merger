from pathlib import Path
from intertext_files_merger.text_merger import get_language_text


def test_merge_text():
    expected_output=Path('./tests/data/t001-output/dmk-t341-t0202.bo.xml').read_text(encoding="utf-8")
    file_paths=['./tests/data/t001-input/dmk-t341-t0202-01-padma-20221217.bo.xml','./tests/data/t001-input/dmk-t341-t0202-03-JC-20221217.bo.xml']
    merged_text=get_language_text(file_paths)
    assert merged_text == expected_output

    expected_output_cn=Path('./tests/data/t001-output/dmk-t341-t0202.cn.xml').read_text(encoding="utf-8")
    file_paths_cn=['./tests/data/t001-input/dmk-t341-t0202-01-padma-20221217.cn.xml','./tests/data/t001-input/dmk-t341-t0202-03-JC-20221217.cn.xml']
    merged_text_cn=get_language_text(file_paths_cn)
    assert merged_text_cn == expected_output_cn

