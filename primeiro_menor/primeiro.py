
def primeiro_menor(num,numeros):
	ind = -1
	for i in range(len(numeros)):
		if int(numeros[i]) < num:
			ind = i
			break
	
	return ind

def main():
	seq = input()
	l = seq.split()
	n = int(input())
	if primeiro_menor(n,l) == -1:
		print('sem menores que {}'.format(n))
	else:
		print('primeiro menor que {}: {}'.format(n,l[primeiro_menor(n,l)]))  
	


if __name__ == '__main__':
    main()
