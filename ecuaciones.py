from math import sqrt
print("1._ ecuacuacion de primer grado/lineal")
print("2._ ecuacuacion de segungo grado/cuadratica")
opcion = input("\n Elige una opción del menú   :")

if opcion == "1":
    # mostramos un mensaje de bienvenida
    print('ecuación de segundo grado:')
    print('    ax² + bx + c = 0')

    # pedimos los coeficientes al usuario
    a, b, c = [float(input(f'Dame el coeficiente {coef}: ')) for coef in ('a', 'b', 'c')]

    # calculamos el discriminante
    discriminante =  b * b - 4 * a * c

    if discriminante < 0: # comprobamos si no existen soluciones reales
        print(f'La ecuación no tiene soluciones reales.')
    else:
        raiz = sqrt(discriminante)      # calculamos la raíz
        x_1 = (-b + raiz) / (2 * a)     # calculamos una primera solución
        if discriminante != 0:          # comprobamos si hay otra solución
            x_2 = (-b - raiz) / (2 * a) # calculamos la segunda solución
            print(f'Las soluciones son {x_1} y {x_2}.') # mostramos las dos soluciones
        else:
            print(f'La única solución es x = {x_1}') # mostramos la única solución

if opcion =="2":
    a = float(input('Valor de a: '))
    b = float(input('Valor de b: '))

    if a != 0:
        x = (-b/a)
   
        print ('Solucion de la ecuacion: x=%4.3f  ' % (x))
    else:
        if  a == 0 and  b != 0:
            print ('la ecuacion no tiene solucion:')
        else:
            print ('La ecuacion tiene infinitas soluciones. ')


