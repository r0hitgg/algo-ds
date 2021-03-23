def permute(count, perm_list):
    if count == 1:
        return perm_list
    else:
        return [
            x + y
            for x in perm_list
            for y in permute(count-1, perm_list)
        ]


print(permute(2, ['a', 'b', 'c']))
