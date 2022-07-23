# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/23 17:42
# Tool ：IntelliJ IDEA
import pytest


def add_function(a: int, b: int) -> int:
    return a + b


@pytest.mark.parametrize(["a", "b", "expected"], [(3, 5, 8), (2, 7, 9), (5, 5, 10)], ids=["case1", "case2", "case3"])
def test_add(a: int, b: int, expected: int) -> None:
    assert add_function(a, b) == expected


@pytest.mark.parametrize("a", [0, 1, 5])
@pytest.mark.parametrize("b", [2, 3, 10])
def test_add2(a: int, b: int) -> None:
    print(f"测试数据组合：a->{a}, b->{b}")
