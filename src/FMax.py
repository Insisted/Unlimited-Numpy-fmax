from itertools import zip_longest as lzip

class FMax(object):
  _FILTER = lambda self, y: map(lambda x: [0, x][isinstance(x, (int, float))], y)
  
  def __init__(self, lst):
    self.lst = self._FILTER(lst)

  def fmax(self, *args):
    arg = self._filter(args)
    longest = lzip(self.lst, *arg, fillvalue=0)
    
    return list(map(max, longest))

  def _filter(self, arg):
    arr = []
    
    for i in arg:
      if isinstance(i, set):
        arr.append(sorted(self._FILTER(i)))
      elif isinstance(i, (list, tuple, dict, {}.keys().__class__, {}.values().__class__)):
        arr.append(self._FILTER(i))
      elif isinstance(i, {}.items().__class__):
        arr.append(self._FILTER(map(lambda x: x[1], args[2])))
      else:
        arr.append([])
    
    return arr


if __name__ == '__main__':
  a = [1, 4, 5, 3, 4, '1']
  b = (2, 6, 3, 5, '1')
  c = {4, 5, 3}
  d = {3: 10, 50: 4, 4:3}

  fmax = FMax(a)
  print(fmax.fmax(b, c, d, '6'))
