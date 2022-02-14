#Ejercicio 1

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print('There are', len(planets), 'planets')

planets.append('Pluto')

print(planets[-1], 'is the last planet')

#Ejercicio 2
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
user_planet = input('Please enter the name of the planet (with a capital letter to start)')

planet_index = planets.index(user_planet)

print('Here are the planets closer than ' + user_planet)
print(planets[0:planet_index])

print('Here are the planets further than ' + user_planet)
print(planets[planet_index + 1:])