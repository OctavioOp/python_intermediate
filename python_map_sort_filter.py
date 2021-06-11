objetos = [

    {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male"
    },
    {
        "name": "Wilhuff Tarkin",
        "height": "180",
        "mass": "unknown",
        "hair_color": "auburn, grey",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "64BBY",
        "gender": "male"
    },
    {
        "name": "Yoda",
        "height": "66",
        "mass": "17",
        "hair_color": "white",
        "skin_color": "green",
        "eye_color": "brown",
        "birth_year": "896BBY",
        "gender": "male"
    },
    {
        "name": "Padmé Amidala",
        "height": "185",
        "mass": "45",
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": "46BBY",
        "gender": "female"
    }

]
#Obtener la lista de nombres, altura y peso //map
#Ordenar por estatura //sort
#filtrar solo mayores 180 cm height //filter

valorMap = map((lambda x : (x['name'] , x['eye_color'])), objetos)
valorMap = [valorMap for valorMap in valorMap]
print(valorMap)

valores =  filter((lambda x: int(x['height']) >= 180), objetos)
valores = [valores for valores in valores]
print(valores)

valorSort = sorted(objetos, key=lambda x : x['height'], reverse=True)
valorSort = [valorSort for valorSort in valorSort]
print(valorSort)



