from unittest import mock, TestCase, main
from archub import cmdline


class TestCmdlineProg(TestCase):
    def setUp(self):
        self.cut = cmdline.prog

    def test_works_when_file_ends_with_dotpy(self):
        with mock.patch('sys.argv', ['ah']):
            self.assertEqual('ah test', self.cut('test.py'))

    def test_works_when_file_ends_with_dotpyc(self):
        with mock.patch('sys.argv', ['ah']):
            self.assertEqual('ah test', self.cut('test.pyc'))


if '__main__' == __name__:
    main()
