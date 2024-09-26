set_countries = {'arg', 'tur', 'bol' }

size = len (set_countries)
print(size)

print('arg' in set_countries)
print('mex' in set_countries)

#add 
set_countries.add('mex')
print(set_countries)
set_countries.add('mex')
print(set_countries)

#update
set_countries.update({'ecua', 'pe'})
print(set_countries)

#remove
set_countries.remove('pe')
print(set_countries)

set_countries.clear()
print(set_countries)
print(len(set_countries))