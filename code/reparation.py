
def poids(s, bin):
	pds = 0
	for obj in bin:
		pds = pds + s[obj]

	return pds

def reparation(instance, ouvert, sac, coef):

	s = list()

	for i in range(instance.nb_obj_diff):
		for j in range(instance.obj_nb[i]):
			s.append(instance.obj_taille[i])

	bins = list()

	objMis = [False for _ in range(instance.nb_obj_tot)]

	if(ouvert):
		tailleDict = {i : [] for i in instance.obj_taille}
		for ind, obj in enumerate(s):
			tailleDict[obj].append(ind)

		bin = [ind for ind, obj in enumerate(sac) if obj == True]

		tailleBin = {i : 0 for i in instance.obj_taille}

		for obj in bin:
			tailleBin[s[obj]] += 1

		temp = {taille: 0 for taille in instance.obj_taille}
		for obj in bin:
			temp[s[obj]] = int(len(tailleDict[s[obj]])/tailleBin[s[obj]])

		minimum = min([temp[i] for i in temp if temp[i] > 0])
		bins.append(bin)

		for obj in bin:
			objMis[obj] = True
			ind = tailleDict[s[obj]].index(obj)
			tailleDict[s[obj]].pop(ind)

		for i in range(minimum - 1):
			newBin = list()
			for obj in bin:
				o = tailleDict[s[obj]].pop(0)
				newBin.append(o)
				objMis[o] = True
			bins.append(newBin)

	objTrie = sorted(range(instance.nb_obj_tot), key=lambda k: coef[k], reverse=True)

	for obj in objTrie:
		if(not(objMis[obj])):
			for b in bins:
				if(s[obj] + poids(s, b) <= instance.cap):
					b.append(obj)
					objMis[obj] = True
					break
			if(not(objMis[obj])):
				bins.append([obj])
			objMis[obj] = True

	return bins
