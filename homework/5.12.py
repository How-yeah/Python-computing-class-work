def sorted(iterable: list, reverse=False) -> list:
    result = []
    iterable_copy = iterable[:]
    if not reverse:
        while iterable_copy:
            min_elem = min(iterable_copy)
            result.append(min_elem)
            iterable_copy.remove(min_elem)
    else:
        while iterable_copy:
            max_elem = max(iterable_copy)
            result.append(max_elem)
            iterable_copy.remove(max_elem)
    return result


a = [4, 5, 2, 1, 6, 2, 8, 9]
print(sorted(a))
