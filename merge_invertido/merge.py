def merge_invertido(l1, l2):
	i = len(l1) - 1
	j = len(l2) - 1
	n = []
	while True:
		if i < 0 or j < 0:
			break
		if l1[i] >= l2[j]:
			n.append(l1[i])
			i -= 1
		else:
			n.append(l2[j])
			j -= 1
			
	if i < 0:
		for k in range(j,-1,-1):
			n.append(l2[k])
	else:
		for k in range(i,-1,-1):
			n.append(l1[k])
	
	return n


