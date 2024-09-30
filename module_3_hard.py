data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def cont (data):
    cont_ = 0


    def recurse (i):
        nonlocal cont_
        if isinstance(i, (int, float)):
            cont_ += i
        elif isinstance(i, str):
            cont_ += len(i)
        elif isinstance(i, (list, set, tuple)):
            for i_ in i:
                recurse(i_)
        elif isinstance(i, dict):
            for key, value, in i.items():
                recurse(key)
                recurse(value)


    recurse(data)
    return cont_                               


result = cont(data_structure)
print(result)