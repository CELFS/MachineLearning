import unittest
from name_function import get_formatted_name # 新建文件夹，放同一个文件夹下，会报错（无法识别）【why？】【已解决】【main的调用方式不对，参考 unittest 模块的定义】

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') # 断言方法,判断两者是否相等，不相等则说一声

# unittest.main() # 输出不显示 “.” # 【调用方式有误，参考 unittest 的调用形式即可】——这个涉及 python 的程序接口机制
if __name__ == '__main__':
    unittest.main()