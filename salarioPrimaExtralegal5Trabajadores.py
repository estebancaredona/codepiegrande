# @autor: Esteban Marin Cardona
# @fecha: 21/08/2024
# @descripcion: realizar un programa para calcular el salario y la prima extralegal de 5 empleados. los datos a ingrese son: indentificar, nombres, salario base. la prima extralegal se calcula de acuerdo con el salario neto si el salario neto es mayor que 1200000 tiene una prima extralegal del 16%, de lo contrario sera del 7% se debe imprimir por cada empleado: la identificacion, los nombres, el salario base, la deduccion por salud, la deduccion por pension, el salario neto y la prima extralegal. el primer empleado deben ser sus datos reales. por salud se deduce el 4.5% por pension se deduce el 4.0%

for i in range (1, 6):

    identificacion = (input("ingrese indentificacion del empleado: "))
    nombre = (input("ingrese nombre del empleado: "))
    salarioBase = (int(input("ingrese salario base del empleado: ")))

    deduccionSalud = salarioBase*0.045
    deduccionPension = salarioBase*0.04
    salarioNeto = salarioBase - deduccionPension - deduccionSalud
    
    if salarioNeto < 1200000:
        primaExtralegal = salarioNeto * 0.16
    else:
        primaExtralegal = salarioNeto * 0.07
    
    print(f"Nombre: {nombre}")
    print(f"Identificación: {identificacion}")
    print(f"Salario base: {salarioBase}")
    print(f"Deducción por salud: {deduccionSalud}")
    print(f"Deducción por pensión: {deduccionPension}")
    print(f"Salario neto: {salarioNeto}")
    print(f"Prima extralegal: {primaExtralegal}")




