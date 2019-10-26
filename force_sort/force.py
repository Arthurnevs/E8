def force_sort(l):
  aux = []
  for j in range(len(l)):
    aux.append(l[j])

  for i in range(len(l)-1):
    if l[i] > l[i+1]:
      l[i+1] = l[i]

  k = 0
  nova = []
  while True:
    if k == len(aux):
      break
    v = l[k] - aux[k]
    nova.append(v)
    k += 1
  
  return nova


