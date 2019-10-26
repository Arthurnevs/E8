def separa_duas_cores(l,cor1,cor2):
  for i in range(len(l)):
    if l[i] == cor1:
      for j in range(i,-1,-1):
        if j == 0:
          break
        l[j],l[j-1] = l[j-1],l[j]

