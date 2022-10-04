from typing import List
import unittest
import _scanner

  
class TestIfList(unittest.TestCase):
    
    # Returns 'ok' if the scanner returns a list.
    def test_the_scanner(self):
        pt = [23,445,3389]
        self.assertEqual( type(_scanner.scan_now('8.8.8.8', pt)), list)
        self.assertEqual( type(_scanner.scan_now('127.0.0.0', pt)), list)
        self.assertEqual( type(_scanner.scan_now('20.220.195.124', pt)), list)
        self.assertEqual( type(_scanner.scan_now('8.8.8.8', pt)), list)


if __name__ == '__main__':
   unittest.main()