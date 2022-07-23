# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/23 19:01
# Tool ：IntelliJ IDEA
import pytest


class TestDemo:
    @pytest.mark.demo
    def test_case1(self):
        print(f"testcase01")

    @pytest.mark.demo
    @pytest.mark.smoke
    def test_case2(self):
        print(f"testcase02")
