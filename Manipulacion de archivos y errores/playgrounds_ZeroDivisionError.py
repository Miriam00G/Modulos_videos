def my_divide(a, b):
    
    try:
        result = a / b
    except ZeroDivisionError:
        result = 'No se puede dividir por 0'
    return result

response = my_divide(10, 2)
print(response)

response = my_divide(10, 0)
print(response)