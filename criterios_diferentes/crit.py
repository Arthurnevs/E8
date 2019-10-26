
def ordena(l1,l2):
  n = []

  i = 0
  j = len(l2)-1

  while True:
    if i == len(l1) or j == -1:
      break
    
    if l1[i] > l2[j]:
      n.append(l2[j])
      j -= 1
    else:
      n.append(l1[i])
      i += 1


  if i != len(l1):
    for k in range(i,len(l1)):
      n.append(l1[k])
  else:
    for m in range(len(l2)-1,-1,-1):
      n.append(l2[m])

  return n  


