import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
insere_ordenado_primeiro = getattr(undertest, 'insere_ordenado_primeiro', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        l1 = [5,2,6,9,11,13]
        insere_ordenado_primeiro(l1)
        assert l1 == [2,5,6,9,11,13]

    def test_outro(self):
        l2 = [3,1,2,4]
        insere_ordenado_primeiro(l2)
        assert l2 == [1,2,3,4]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
