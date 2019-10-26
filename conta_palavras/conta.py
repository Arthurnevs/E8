
def conta_palavras(k, palavras):
  l = palavras.split(':')
  c = 0
  for i in range(len(l)):
    if len(l[i]) >= k:
      c += 1
  
  return c


