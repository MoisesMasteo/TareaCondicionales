Primer_numero = int(input("Cuál es el primer nñúmero? "))
Segundo_numero = int(input("Cuál es el segundo número? "))
Tercer_numero = int(input("Cuál es el tercer número? "))

if (Primer_numero == Segundo_numero == Tercer_numero):
    print("Las tres números son iguales.")
elif (Primer_numero > Segundo_numero and Primer_numero > Tercer_numero):
    print("El número más grande es :", Primer_numero)
elif (Segundo_numero > Primer_numero and Segundo_numero > Tercer_numero):
    print("El número más grande es:", Segundo_numero)
else:
    print ("El número más grande es: ", Tercer_numero)
