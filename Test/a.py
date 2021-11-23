import unittest

def formatIt(first, middle, last):
  return f"{first.title()} {middle.title()} {last.title()}"


class Testing(unittest.TestCase):
  def test_fun1(self):
    ret = formatIt('dipankar', 'kumar', 'das')
    self.assertEquals(ret, "Dipankar Kumar Das")


if __name__ == '__main__':
  unittest.main()