a_list=[]
with open('../test.txt', encoding='utf-8') as f:
	for line in f:
		a_list.append(line.strip('\n').split(',')[0])
print(a_list)
from collections import Counter 
res = Counter(a_list) 
print(res) 

    