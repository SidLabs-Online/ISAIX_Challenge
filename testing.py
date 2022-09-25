
import unittest
import _scanner

  
class TestIfList(unittest.TestCase):
    
    # Returns 'ok' if the scanner returns a list.
    def test_the_scanner(self):

        self.assertEqual( type(_scanner.scan_now('8.8.8.8')), dict)
        self.assertEqual( type(_scanner.scan_now('127.0.0.0')), dict)
        self.assertEqual( type(_scanner.scan_now('20.220.195.124')), dict)
        self.assertEqual( type(_scanner.scan_now('8.8.8.8')), dict)


if __name__ == '__main__':
   unittest.main()