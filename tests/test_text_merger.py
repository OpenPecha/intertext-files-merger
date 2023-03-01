from pathlib import Path
from intertext_files_merger.text_merger import get_language_text


expected_output=Path('./tests/data/t001-output/t001.bo.xml').read_text(encoding="utf-8")

def test_merge_text():
    data=['./tests/data/t001-input/t001-01-padma.bo.xml','./tests/data/t001-input/t001-03-jc.bo.xml']
    merged_text=get_language_text(data)
    #Path('./tests/merged_text.xml').write_text(merged_text,encoding='utf-8')
    assert merged_text == expected_output