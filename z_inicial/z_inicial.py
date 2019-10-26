
def z_inicial(l):
	c = 0 
	for i in range(len(l)):
		if l[i][0] == 'z' or l[i][0] == 'Z':
			c += 1
	
	return c

s = input()
l = s.split()
print(z_inicial(l))
			
