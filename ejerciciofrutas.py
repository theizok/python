frutas = {'Banano':4500, 'Manzana':9071, 'Pera':5110, 'Sandia':3000, 'Papaya':5200, 'Uva':8500}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, 'COP$')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")