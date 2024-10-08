with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('Nuevas cosas en este archivo\n')
    file.write('otra linea mas\n')
    file.write('otra mas\n')
               
               
               
               
               