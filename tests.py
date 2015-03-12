import unittest
import bbtourn


class TestFileFunctions(unittest.TestCase):
//Test to see if you were able to get data from the file   
    def test_getdata(self):
        element = bbtourn.getTeam()
        self.assertEqual(element.empty, False )


if __name__ == '__main__':
    unittest.main()
