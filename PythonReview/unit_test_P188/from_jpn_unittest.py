import unittest

def get_formatted_name(first, middle, last):
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title() # 首字母大写

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()