def cadastra(fila,nome,prior):
  
  aux = []
  aux.append(nome)
  aux.append(prior)
  fila.append(aux)

  for i in range(len(fila)-1,-1,-1):
    if fila[i][1] == 'vermelho':
      if i == 0:
        break
      if fila[i-1][1] == 'vermelho':
        break
      else:
        fila[i],fila[i-1] = fila[i-1],fila[i]

    
    elif fila[i][1] == 'laranja':
      if i == 0:
        break
      if fila[i-1][1] == 'vermelho' or fila[i-1][1] == 'laranja':
        break
      else:
        fila[i],fila[i-1] = fila[i-1],fila[i]
    
    elif fila[i][1] == 'amarelo':
      if i == 0:
        break
      if fila[i-1][1] == 'vermelho' or fila[i-1][1] == 'laranja' or fila[i-1][1] == 'amarelo':
        break
      else:
        fila[i],fila[i-1] = fila[i-1],fila[i]
    
    elif fila[i][1] == 'verde':
      if i == 0:
        break
      if fila[i-1][1] == 'vermelho' or fila[i-1][1] == 'laranja' or fila[i-1][1] == 'amarelo' or fila[i-1][1] == 'verde':
        break
      else:
        fila[i],fila[i-1] = fila[i-1],fila[i]
    else:
      break


def resumo():
  v = 0
  lar = 0
  a = 0
  verd = 0
  azu = 0

  for k in range(len(fila)):
    if fila[k][1] == 'vermelho':
      v += 1
    elif fila[k][1] == 'laranja':
      lar += 1
    elif fila[k][1] == 'amarelo':
      a += 1
    elif fila[k][1] == 'verde':
      verd += 1
    else:
      azu += 1
    
  print('---')
  print('vermelho: {}'.format(v))
  print('laranja: {}'.format(lar))
  print('amarelo: {}'.format(a))
  print('verde: {}'.format(verd))
  print('azul: {}'.format(azu))
  print('---') 

fila = []
while True:
  p = input()
  if p == 'fim':
    break
  l = p.split()
  cadastra(fila,l[0],l[1])

for j in range(len(fila)):
  print(fila[j][0])

resumo()
