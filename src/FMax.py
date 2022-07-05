from itertools import zip_longest as lzip

class FMax(object):
  FILTER = lambda self, y: filter(lambda x: isinstance(x, (int, float)), y)
  
  def __init__(self, lst):
    self.lst = self.FILTER(lst)

  def fmax(self, *args):
    args = self._filter(args)
    longest = lzip(self.lst, *args, fillvalue=0)
    
    return list(map(max, longest))

  def _filter(self, *args):
    a = []
    
    for i in args:
      if isinstance(i, set):
        a.append(sorted(self.FILTER(i)))
      elif isinstance(i, (list, tuple, dict)):
        a.append(self.FILTER(i))
      else:
        a.append([])
    
    return a


if __name__ == '__main__':
  a = [1, 4, 5, 3, 4, '1']
  b = (2, 6, 3, 5, '1')
  c = {4, 5, 3}
  d = {3: 10, 50: 4, 4:3}

  obj = FMax(a)
  print(obj.fmax(b, c, d, "6"))
