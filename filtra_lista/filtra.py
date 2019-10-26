
def filtra_lista(num, l):
	n = []
	for i in range(len(l)):
		if i % num == 0:
			n.append(l[i])
	return n
			

