def drop_duplicates(seq):
    if isinstance(seq, list):
        # 转集合, 再转回列表
        return list(set(seq))
    if isinstance(seq, dict):
        def reverse_dict(_dict):
            # 将键值互换, 并使字典逆序
            return dict(zip(list(_dict.values())[::-1], list(_dict.keys())[::-1]))

        return reverse_dict(reverse_dict(seq))


a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print(drop_duplicates(a))

b = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 2, 'g': 3, 'h': 4}
print(drop_duplicates(b))
