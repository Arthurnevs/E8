def insere_ordenado_primeiro(l):
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			l[i],l[i+1] = l[i+1],l[i]
		else:
			break

