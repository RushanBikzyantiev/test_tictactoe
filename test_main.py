import unittest
from main import check_win
board1=[]
class MyTestCase(unittest.TestCase):
    
    def test_check_win(self):
        self.assertEqual(check_win(['X', 'X', 'X', 4, 'O', 6, 7, 8, 'O']), 'X')
        

if __name__ == '__main__':
    unittest.main()
