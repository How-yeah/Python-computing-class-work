from random import randint


def remove(sequence):
    if isinstance(sequence, list):  # 处理列表中重复的元素
        temp = set()
        sequence.reverse()
        for i in range(len(sequence) - 1, -1, -1):
            if sequence[i] not in temp:
                temp.add(sequence[i])
            else:
                del sequence[i]
        sequence.reverse()
        return sequence
    elif isinstance(sequence, dict):  # 处理字典中重复的值
        temp = set()
        tempKeys = list(sequence.keys())
        tempValues = list(sequence.values())
        for i in range(len(tempValues) - 1):
            if tempValues[i] not in temp:
                temp.add(tempValues[i])
            else:
                del tempKeys[i]
                del tempValues[i]
                i -= 1
        sequence = dict(zip(tempKeys, tempValues))
        return sequence


List = [randint(1, 10) for i in range(100)]
print(List)
print(remove(List))
Dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(Dict)
print(remove(Dict))
