# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/23 22:10
# Tool ：IntelliJ IDEA
import pytest


@pytest.fixture()
def my_fixture():
    print("执行my_fixture")
