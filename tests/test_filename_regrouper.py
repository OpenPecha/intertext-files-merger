from intertext_files_merger.filename_regrouper import regroup_filename

expected_output = {
    "t001":
    {
    'bo':[
    "t001-01-padma.bo.xml",
    "t001-03-jc.bo.xml"],
    'cn':[
    "t001-01-padma.cn.xml",
    "t001-03-jc.cn.xml"
    ],
    'bo.cn':[
    "t001-01-padma.bo.cn.xml",
    "t001-03-jc.bo.cn.xml"
    ]
    }
}


def test_regroup_filename():
    input_dir = '/home/baller/work/intertext-files-merger/tests/data/t001-input'
    regrouped_filename = regroup_filename(input_dir)
    assert regrouped_filename == expected_output


if __name__ == "__main__":
    test_regroup_filename()
