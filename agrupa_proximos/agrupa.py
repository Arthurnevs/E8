
def agrupa_proximos(l, valor, criterio):
	nova = []
	for i in range(len(l)):
		if valor - l[i] < criterio and valor - l[i] > criterio * -1:
			nova.append(l[i])
	
	return nova
			
l = [1,2,3,4,8,22,3,5]
print(agrupa_proximos(l,4,2))

