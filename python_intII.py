    # Actualiza los valores en diccionarios y listas
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael',
     'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

'''
Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
En el directorio sports_directory, cambia 'Messi' a 'Andres'
Camba el valor 20 en z a 30'''
# 1
x[1][0] = 15
print(x)

# 2
students[0].update({'last_name': 'Bryant'})
print(students)

# 3
socc = sports_directory.get('soccer')
socc[0] = 'Andres'
print(socc)

sports_directory.update({'soccer': socc})
print(sports_directory)

# 4
z[0].update({'y': 30})
print(z)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
'''

# La salida debería ser: (Está bien si cada clave y valor quedan en dos líneas separadas)
# Bonus: Hacer que aparezcan exactamente así!
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''


def iterateDictionary(students):
    for student in students:
        print(
            f"first_name - {student['first_name']}, last_name - {student['last_name']}")


iterateDictionary(students)


def iterateDictionary2(lst):
    for elem in lst:
        str_elem = []

        for key, value in elem.items():
            str_elem.append(f"{key} - {value}")
        print(', '.join(str_elem))


iterateDictionary2(students)

'''Obtén valores de una lista de diccionarios
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
'''
key_name = 'first_name'
key_name1 = 'last_name'


def iterateDictionary3(key_name, some_list):
    for lst in some_list:
        print(f"{lst[key_name]}")


iterateDictionary3(key_name, students)
iterateDictionary3(key_name1, students)

'''Itera a través de un diccionario con valores de listas
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todas listas, 
imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados
dentro de la lista de cada clave.'''

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):

    print(str(len(some_dict['locations'])) + ' Locations')
    for i in range(0 , len(some_dict['locations'])):
        print(some_dict['locations'][i])
    print(' ')
    print(str(len(some_dict['instructors'])) + ' instructors')
    for i in range(0 , len(some_dict['instructors'])):
        print(some_dict['instructors'][i])


printInfo(dojo)
