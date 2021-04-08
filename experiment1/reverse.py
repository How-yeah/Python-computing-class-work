a_list=[]
b_list=[]
with open(r'./experiment1/data/words.txt') as f:
	for line in f:
		a_list.append(line.strip('\n').split(',')[0])
for i in a_list:
    result=i[::-1]
    if i==result:          #若它反转后与它本身相同，则不输出
        continue
    for j in a_list:
        if result==j and i + '和' + j not in b_list:
            print(i,'和',j,';')
            b_list.append(i + '和' + j)




