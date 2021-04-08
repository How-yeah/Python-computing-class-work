a_list=[]
with open(r'./experiment1/data/words.txt') as f:
	for line in f:
		a_list.append(line.strip('\n').split(',')[0])
for i in a_list:
    result=i[::-1]
    for j in a_list:
        if result==j:
            print(i,'和',j,';')




