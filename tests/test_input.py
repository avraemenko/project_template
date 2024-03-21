import unittest
from ..app.io.input import read_from_file_builtin, read_from_file_pandas

class TestInputFunctions(unittest.TestCase):
    def test_read_from_file_builtin(self):
        expected_content = "Hello, world!"
        content = read_from_file_builtin('data/test.txt')
        self.assertEqual(content, expected_content)

    def test_read_from_file_builtin_empty(self):
        expected_content = ""
        content = read_from_file_builtin('data/test_empty.txt')
        self.assertEqual(content, expected_content)

    def test_read_from_file_pandas(self):
        expected_content = "id,name\n1,Test\n"
        content = read_from_file_pandas('data/test.csv').to_csv(index=False).strip()
        self.assertEqual(content, expected_content)

    def test_read_from_file_pandas_empty(self):
        expected_content = "id,name"
        content = read_from_file_pandas('data/test_empty.csv').to_csv(index=False).strip()
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()
