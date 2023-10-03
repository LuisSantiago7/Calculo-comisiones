''' en una empresa, los vendedores reciben comicsiones del 13% de ventas totales, se requiere que ayudes a calcular sus comisiones. crea un prgrama donde pregunte su nombre y cuanto han vendido en este mes, el programa debe resonder su nombre + el monto que corresponde de comisiones'''


name = input('Cual es tu nombre?\n').capitalize()
last_name = input('Cual es tu apellido?\n').capitalize()
id_empleado = int(input('ingrese ID de empleado:\n'))

while True:
    if name == 'Luis' and last_name == 'Eleazar': 
        if id_empleado == 58471377:
            comision = float(input('Cuanto vendiste este mes?\n'))

            calulo = round(comision * .13, 2)
            print(f'Hola, {name} {last_name}, la suma total de comisiones de este mes es de ${calulo} USD')
            break
        else:
            print('ID incorrecto')
    else: 
        print('Empleado no identificado')
        break