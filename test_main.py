import unittest
from main import check_win
board1=[]
class MyTestCase(unittest.TestCase):
    
    def test_check_win(self):
        self.assertEqual(check_win(['O', 2, 'X', 4, 'O', 'X', 7, 8, 'X']), 'X')
        

if __name__ == '__main__':
    unittest.main()
