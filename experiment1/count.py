a_list=[]
with open(r'./experiment1/data/english.txt') as f:
	str1=f.read()
a_list=str1.split(' ')
print(a_list)
from collections import Counter 
result = Counter(a_list) 
print(result)