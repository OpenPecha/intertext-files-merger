from pathlib import Path
from intertext_files_merger.alignment_merger import get_alignment_text


def test_merge_text():
    expected_output=Path('./tests/data/t001-output/t001.bo.cn.xml').read_text(encoding="utf-8")
    file_paths=["./tests/data/t001-input/dmk-t341-t0202-10-padma-20221217.bo.cn.xml",
                "./tests/data/t001-input/dmk-t341-t0202-11-JC-20221210.bo.cn.xml"]
    merged_alignment=get_alignment_text(file_paths)
    assert merged_alignment == expected_output