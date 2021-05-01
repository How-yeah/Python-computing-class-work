import random

int_list = [random.randint(0, 100) for i in range(1000)]
int_dict = {}
for key in int_list:
    int_dict[key] = int_dict.get(key, 0)+1

for key, value in int_dict.items():
    print(str(key)+': '+str(value))
