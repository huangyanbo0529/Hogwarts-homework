# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/23 22:17
# Tool ：IntelliJ IDEA
import pytest


@pytest.mark.parametrize("a, b, c", [(1, 2, 3)])
def test_case1(a, b, c, my_fixture):
    print("执行testcase1")
    value = my_fixture
    print(value)
    assert a + b == c


@pytest.mark.parametrize("a, b, c", [(1, 2, 3)])
def test_case2(a, b, c):
    print("执行testcase2")
    assert a + b == c


@pytest.mark.parametrize("a, b, c", [(1, 2, 3)])
def test_case3(a, b, c, my_fixture):
    print("执行testcase3")
    value = my_fixture
    print(value)
    assert a + b == c
