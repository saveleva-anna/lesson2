
def string (s1,s2):
  if isinstance(s1,str) != isinstance(s2,str):
    return 0
  elif s1==s2:
    return 1
  elif s1!=s2 and len(s1)>len(s2):
    return 2
  elif s1!=s2 and s2=='learn':
    return 3
print (string(1, 'year'))
print (string('five', 'five'))
print (string('yellow', 'year'))
print (string('len', 'learn'))