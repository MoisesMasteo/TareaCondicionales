edad = int(input("Que edad tienes? "))
if (edad >= 16):
    ingresos = int(input("Cuantos ingresos tienes al mes? "))
    if (ingresos >= 1000):
        print ("Tienes que tributar")
    else:
        print ("Tienes que tener unos ingresos de 1000€ al mes para poder tributar")
else:
    print ("Tienes que ser mayor de 16 años para poder tributar")