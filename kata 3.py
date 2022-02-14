#problema 1
vel_asteroide = 49
if vel_asteroide > 25:
    print('¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!')
else:
    print('¡No hay problema!')

#problema 2
asteroide = 19
if asteroide > 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif asteroide == 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
else:
    print('¡Nada que ver aquí!')

#problema 3
velocidad_asteroide = 25
tamano_asteroide = 40
if velocidad_asteroide > 25 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('Nada que ver aquí')
else:
    print('Nada que ver aquí')