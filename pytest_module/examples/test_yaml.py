# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/23 21:25
# Tool ：IntelliJ IDEA
import pytest
import yaml

from common.base import root_path

file_name = root_path + "\\pytest_module\\examples\\data.yml"


def get_data():
    try:
        f = open(file_name, 'r', encoding="utf-8")
        test_data = yaml.safe_load(f)
        return test_data['data'], test_data['ids'][0]
    except:
        raise Exception("读取yaml文件出现异常!")
    finally:
        f.close()


@pytest.mark.parametrize("a, b, expect", get_data()[0], ids=get_data()[1])
def test_yaml_data(a, b, expect):
    assert a + b == expect
