from pathlib import Path
from intertext_files_merger.alignment_merger import get_alignment_text


def test_merge_text():
    expected_output=Path('./tests/data/t001-output/dmk-t341-t0202.bo.cn.xml').read_text(encoding="utf-8")
    file_paths=[Path('./tests/data/t001-input/dmk-t341-t0202-01-padma-20221217.bo.cn.xml'),Path('./tests/data/t001-input/dmk-t341-t0202-03-JC-20221217.bo.cn.xml')]
    merged_alignment=get_alignment_text(file_paths)
    assert merged_alignment == expected_output