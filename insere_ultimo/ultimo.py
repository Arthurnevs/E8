def insere_ordenado_ultimo(l):
  for i in range(len(l)-1,-1,-1):
    if i == 0:
      break
    if l[i] < l[i-1]:
      l[i],l[i-1] = l[i-1],l[i]
    else:
      break
