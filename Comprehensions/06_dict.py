import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = { country: random.randint(1, 100)
for country in countries}
print(population_v2)

result = { country: population for (country, population) in population_v2.items()
if population > 50}
print(result)

text = 'Hola soy Miryam'
unique = { carac: carac.upper() for carac in text if carac in 'aeiou'}
print(unique)