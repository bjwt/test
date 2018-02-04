import unittest

class Sample(unittest.TestCase):
    def test_a(self):
        assert 1 == 2, 'test print Errors'
        print 'test_a'

if __name__ == '__main__':
    r = unittest.TestResult()
    Sample('test_a').run(result=r)
    print r.__dict__
