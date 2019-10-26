import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
primeiro_menor = getattr(undertest, 'primeiro_menor', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
      assert primeiro_menor(4, [7, 5, 3, 9, 11, 8]) == 2

   def test_exemplo_2(self):
      assert primeiro_menor(3, [7, 5, 3, 9, 11, 8]) == -1

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
