fp = open("lab.txt","r")
for numligne, ligne in enumerate(fp):
	for numColonne, element in enumerate(ligne):
		print (element,numligne,numColonne)


