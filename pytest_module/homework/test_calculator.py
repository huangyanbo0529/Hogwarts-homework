# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/23 18:14
# Tool ：IntelliJ IDEA


"""
【pytest中的setup和teardown用法】
1.模块级（setup_module/teardown_module）开始于模块始末，全局的；
2.函数级（setup_function/teardown_function）只对函数用例生效（不在类中）；
3.类级（setup_class/teardown_class）只在类中前后运行一次(在类中)；
4.方法级（setup_method/teardown_method）开始于方法始末（在类中）；
"""

import pytest

from pytest_module.homework.calculator import Calculator

calculator = Calculator()


def setup_function():
    print(f"开始计算 >>>>函数级别")


def teardown_function():
    print(f"结束计算 >>>>类级别")


@pytest.mark.parametrize("a, b, expected1", [
    (1, 1, 2), (2, 2, 4), (5, 8, 13)
], ids=["case1", "case2", "case3"])
def test_add_func(a, b, expected1):
    assert expected1 == calculator.add(a, b)


@pytest.mark.parametrize("a, b, expected1", [
    (2, 1, 1), (4, 2, 2), (13, 8, 5)
], ids=["case1", "case2", "case3"])
def test_sub_func(a, b, expected1):
    assert expected1 == calculator.sub(a, b)


@pytest.mark.parametrize("a, b, expected1", [
    (2, 1, 2), (2, 2, 4), (5, 8, 40)
], ids=["case1", "case2", "case3"])
def test_mul_func(a, b, expected1):
    assert expected1 == calculator.mul(a, b)


@pytest.mark.parametrize("a, b, expected1", [
    (4, 2, 2), (18, 3, 6), (30, 5, 6)
], ids=["case1", "case2", "case3"])
def test_div_func(a, b, expected1):
    assert expected1 == calculator.div(a, b)


class TestCalculator:
    def setup_class(self):
        self.cal = Calculator()
        print(f"开始计算 >>>>类级别")

    def teardown_class(self):
        print(f"结束计算 >>>>类级别")

    @pytest.mark.parametrize("a, b, expected", [
        (1, 1, 2), (2, 2, 4), (5, 8, 13)
    ], ids=["case1", "case2", "case3"])
    def test_add(self, a, b, expected):
        assert expected == self.cal.add(a, b)

    @pytest.mark.parametrize("a, b, expected", [
        (2, 1, 1), (4, 2, 2), (13, 8, 5)
    ], ids=["case1", "case2", "case3"])
    def test_sub(self, a, b, expected):
        assert expected == self.cal.sub(a, b)

    @pytest.mark.parametrize("a, b, expected", [
        (2, 1, 2), (2, 2, 4), (5, 8, 40)
    ], ids=["case1", "case2", "case3"])
    def test_mul(self, a, b, expected):
        assert expected == self.cal.mul(a, b)

    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 2), (18, 3, 6), (30, 5, 6)
    ], ids=["case1", "case2", "case3"])
    def test_div(self, a, b, expected):
        assert expected == self.cal.div(a, b)
