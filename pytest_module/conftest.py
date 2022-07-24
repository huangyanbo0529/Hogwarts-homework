# _*_coding_*_: utf-8
# Author：yb
# Date ：2022/7/23 22:10
# Tool ：IntelliJ IDEA
import pytest


# autouse默认为False,True自动引用，不需要显示指定
@pytest.fixture(scope="function", autouse=True)
def my_fixture():
    print(f"开始执行my_fixture")
    yield "返回值给调用者"  # 执行到此处函数挂起，直到调用者结束，重新唤醒，继续执行
    print(f"结束执行my_fixture")


def pytest_collection_modifyitems(session, config, items):
    #
    print(type(items))
    # items.reverse()
    # 解决编码问题（中文测试用例名称）
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # if "add" in item._nodeid:
        #     item.add_marker(pytest.mark.add)
        # if "div" in item._nodeid:
        #     item.add_marker(pytest.mark.div)
