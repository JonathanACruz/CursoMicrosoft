#Ejercicio 1
text="Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest"
text_parts = text.split('. ')
text_parts
key_words = ["average", "temperature", "distance"]
for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence)
            break
for sentence in text_parts:
    for key_word in key_words:
        if key_word in sentence:
            print(sentence.replace(' C', ' Celsius'))
            break
    
#Ejercicio 2
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
title = f'datos de gravedad sobre {nombre}'
hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""
template = f"""{title.title()} 
{hechos} 
""" 
print(hechos)
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
print(hechos)
new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))
