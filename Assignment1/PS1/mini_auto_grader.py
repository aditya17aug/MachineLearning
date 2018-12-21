#from __future__ import absolute_import
#from __future__ import division
#from __future__ import print_function

import ID3, parse, random

def testID3AndEvaluate():

  score = 0

  data = [dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]

  if True:
    tree = ID3.ID3(data, 0)
    if tree != None:
      ans = ID3.evaluate(tree, dict(a=1, b=0))
      if ans != 1:
        print("ID3 test 1 failed.")
      else:
        score += 1
        print("ID3 test 1 succeeded.")
    else:
      print("ID3 test 1 failed -- no tree returned")
#  except Exception:
#    print 'ID3 test 1 failed runtime error'

  data = [dict(a=1, b=0, Class=0), dict(a=1, b=1, Class=1)]

  if True:
    tree = ID3.ID3(data, 0)
    if tree != None:
      ans = ID3.evaluate(tree, dict(a=1, b=0))
      if ans != 0:
        print("ID3 test 2 failed.")
      else:
        score += 1
        print("ID3 test 2 succeeded.")
    else:
      print("ID3 test 2 failed -- no tree returned")
#  except Exception:
#    print 'ID3 test 2 failed runtime error'


  data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1),
          dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3),
          dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]

  if True:
    tree = ID3.ID3(data, 0)
    if tree != None:
      ans = ID3.evaluate(tree, dict(a=1, b=0))
      if ans != 2:
        print("ID3 test 3-1 failed.")
      else:
        print("ID3 test 3-1 succeeded.")
        score += 1
      ans = ID3.evaluate(tree, dict(a=1, b=1))
      if ans != 1:
        print("ID3 test 3-2 failed.")
      else:
        print("ID3 test 3-2 succeeded.")
        score += 1
      ans = ID3.evaluate(tree, dict(a=3, b=0))
      if ans != 1:
        print("ID3 test 3-3 failed.")
      else:
        print("ID3 test 3-3 succeeded.")
        score += 1
      ans = ID3.evaluate(tree, dict(a=3, b=1))
      if ans != 3:
        print("ID3 test 3-4 failed.")
      else:
        print("ID3 test 3-4 succeeded.")
        score += 1
    else:
      print("ID3 test 3 failed -- no tree returned")
#  except Exception:
#    print 'ID3 test 3 failed runtime error'

  data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1),
          dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3),
          dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3),
          dict(a=3, b=0, Class=1), dict(a=3, b=0, Class=0)]

  try:
    tree = ID3.ID3(data, 0)
    if tree != None:
      ans = ID3.evaluate(tree, dict(a=3, b=0))
      if ans != 1:
        print("ID3 test 4 failed.")
      else:
        score += 1
        print("ID3 test 4 succeeded.")
    else:
      print("ID3 test 4 failed -- no tree returned")
  except Exception:
    print('ID3 test 4 failed runtime error')


  data = [dict(a=1, b=0, c=0, Class=1), dict(a=1, b=3, c=2, Class=1),
          dict(a=2, b=1, c=1, Class=2), dict(a=2, b=1, c=3, Class=2),
          dict(a=3, b=0, c=1, Class=3), dict(a=3, b=2, c=2, Class=3)]

  try:
    tree = ID3.ID3(data, 0)
    if tree != None:
      ans = ID3.evaluate(tree, dict(a=1, b=1, c=1))
      if ans != 1:
        print("ID3 test 5-1 failed.")
      else:
        score += 1
        print("ID3 test 5-1 succeeded.")
      ans = ID3.evaluate(tree, dict(a=2, b=0, c=0))
      if ans != 2:
        print("ID3 test 5-2 failed.")
      else:
        score += 1
        print("ID3 test 5-2 succeeded.")
      ans = ID3.evaluate(tree, dict(a=3, b=3, c=3))
      if ans != 3:
        print("ID3 test 5-3 failed.")
      else:
        score += 1
        print("ID3 test 5-3 succeeded.")
    else:
      print("ID3 test 5 failed -- no tree returned")
  except Exception:
    print('ID3 test 5 failed runtime error')


  data = [dict(a=1, b=0, c='?', Class=1), dict(a=1, b=3, c=2, Class=1),
         dict(a=2, b='?', c=1, Class=2), dict(a=2, b=1, c=3, Class=2),
         dict(a=3, b=0, c=1, Class=3), dict(a=3, b=2, c='?', Class=3)]

  try:
    tree = ID3.ID3(data, 0)
    if tree != None:
      ans = ID3.evaluate(tree, dict(a=1, b=1, c=1))
      if ans != 1:
        print("ID3 test 6-1 failed.")
      else:
        score += 1
        print("ID3 test 6-1 succeeded.")
      ans = ID3.evaluate(tree, dict(a=2, b=0, c=0))
      if ans != 2:
        print("ID3 test 6-2 failed.")
      else:
        score += 1
        print("ID3 test 6-2 succeeded.")
      ans = ID3.evaluate(tree, dict(a=3, b=3, c=3))
      if ans != 3:
        print("ID3 test 6-3 failed.")
      else:
        score += 1
        print("ID3 test 6-3 succeeded.")
      ans = ID3.evaluate(tree, dict(a=3, b='?', c='?'))
      if ans != 3:
        print("ID3 test 6-4 failed.")
      else:
        score += 1
        print("ID3 test 6-4 succeeded.")
    else:
      print("ID3 test 6 failed -- no tree returned")
  except Exception:
    print('ID3 test 6 failed runtime error')

  data = [dict(a=1, b =0, c =0, d = 1, e = 1, f =3, g =0, h=1, i =0, j =0, Class =1),
          dict(a=1, b =0, c =0, d = 1, e = 2, f =1, g =0, h=0, i =1, j =-2, Class =0),
          dict(a=0, b =1, c =0, d = 0, e = 1, f =1, g =0, h=0, i =5, j =0, Class =1),
          dict(a=1, b =0, c =1, d = 1, e = 2, f =1, g =0, h=0, i =1, j =5, Class =1),
          dict(a=1, b =0, c =1, d = 0, e = 2, f =3, g =0, h=1, i =0, j =60, Class =0),
          dict(a=0, b =1, c =0, d = 1, e = 1, f =2, g =1, h=1, i =7, j =0, Class =1),
          dict(a=0, b =1, c =0, d = 0, e = 0, f =1, g =1, h=0, i =5, j =0, Class =0),
          dict(a=0, b =0, c =0, d = 1, e = 1, f =2, g =1, h=1, i =1, j =0, Class =1),
          dict(a=0, b =1, c =1, d = 0, e = 2, f =1, g =1, h=0, i =5, j =60, Class =0),
          dict(a=1, b =1, c =1, d = 1, e = 2, f =3, g =0, h=1, i =7, j =5, Class =0),
          dict(a=0, b =0, c =0, d = 0, e = 0, f =1, g =0, h=0, i =1, j =0, Class =0),
          dict(a=1, b =1, c =1, d = 1, e = 2, f =1, g =0, h=0, i =5, j =-2, Class =1)]

  try:
    tree = ID3.ID3(data, 0)

    if tree != None:
      ans = ID3.evaluate(tree, dict(a=1, b =0, c =0, d = 1, e = 2, f =1, g =0, h=0, i =1, j =-2))
      if ans == 0:
        score += 2
        print("ID3 test 7-1 succeeded.")
      else:
        print("ID3 test 7-1 failed.")

      ans = ID3.evaluate(tree, dict(a=0, b =1, c =1, d = 0, e = 2, f =1, g =1, h=0, i =5, j =60))
      if ans == 0:
        score += 2
        print("ID3 test 7-2 succeeded.")
      else:
        print("ID3 test 7-2 failed.")

      ans = ID3.evaluate(tree, dict(a=1, b =1, c =1, d = 1, e = 2, f =1, g =0, h=0, i =5, j =-2))
      if ans == 1:
        score += 2
        print("ID3 test 7-3 succeeded.")
      else:
        print("ID3 test 7-3 failed.")
    else:
        print("ID3 test 7-1 failed.")
        print("ID3 test 7-2 failed.")
        print("ID3 test 7-3 failed.")
  except Exception:
    print('ID3 test 7 failed runtime error')
  print("Total Score for Code: ",str(float(score)/20.0*10.0))





if __name__ == "__main__":
    testID3AndEvaluate()
#    testPruning()
