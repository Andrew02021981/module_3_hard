def calculate_structure_sum(data_structure,*args):
    sum_ = 0
    for i in data_structure:
        if type(i) is list or type(i) is tuple:
            sum_ = sum_ + calculate_structure_sum(i)
        elif type(i) is int:
            sum_ = sum_ + i
        elif type(i) is str:
            sum_ = sum_ + len(i)
        elif type(i) is dict:
           sum_ = sum_ + calculate_structure_sum(i.items())
        elif type(i) is set:
            sum_ = sum_ + calculate_structure_sum(list(i))
    return sum_


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

