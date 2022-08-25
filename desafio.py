dados = []
dados.append((1, 'Orlando', 'Fatec Araras'))
dados.append((2, 'Nilton', 'Fatec Araras'))
dados.append(10)
dados.append((3, 'João', 'Fatec Araras'))
dados.append(30.4)
dados.append([1,2,3])
dados.append([])
dados.append([[1, 2, 3], [4, 5, 6]])
dados.append(())
dados.append((4, 'Zenaide', 'Fatec Araras'))
dados.append((1,2,3))
dados.append((5, 'Leonardo', 'Fatec Araras'))
dados.append(())

'''
Crie um programa que imprima somente os nomes dos professores.
A Estrutura de dado com os campos que queremos possui a seguinte estrutura:
(<numero>, <nome>, <unidade>)
'''

for i in dados:
    if type(i) == tuple:
        if len(i) == 3:
            if type(i[1]) == str:
                print(i[1])


for i in dados: 
    try: 
        print(i[1]) 
    except TypeError: 
        pass 
    except IndexError: 
        print('Erro de index') 
