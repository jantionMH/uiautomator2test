from sqlite3.dbapi2 import connect
from pytest_selenium import selenium
import pytest

# 执行Test开头
# @pytest.mark.xfail
def test_01(selenium):
    print('这是test01')
    assert ('test01') == 'test02'
    # pytest.fail(msg='测试失败')

@pytest.mark.skip(reason='尚未完成')
def test_02(self):
    with pytest.raises(AssertionError) as e:
        a = '这是test02'
        print(e.value.args)
    assert e.value == 'test01'

@pytest.mark.finish
def test_03(self):
    print('这是test03')
    assert ('test03') == 'test03'

@pytest.mark.parametrize('username', ['1', '2', '3', ''])
def test_04(self, username):
    assert username != ''
