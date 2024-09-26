set_A = {'arg', 'tur', 'bol'}
set_B = {'ecua', 'bol'}

set_C = set_A.union(set_B)
print(set_C)
print(set_A | set_B)

set_C = set_A.intersection(set_B)
print(set_C)
print(set_A & set_B)

set_C = set_A.difference(set_B)
print(set_C)
print(set_A - set_B) 

set_C = set_A.symmetric_difference(set_B)
print(set_C)
print(set_A ^ set_B)