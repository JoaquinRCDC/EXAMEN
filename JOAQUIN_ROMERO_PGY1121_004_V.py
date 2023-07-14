#JOAQUIN ROMERO CARDENAS PGY1121_004_V


from itertools import cycle



def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11

compra = {
    1:3800,
    2:3000,
    3:2800,
    4:3500,
}


    
def menu():

    while True:
        print('\n-------- Menu "CASA FELIZ" -------\n1. Comprar departamento\n2. Mostrar departamentos disponibles\n3. Ver listado de compradores\n4. Mostrar ganancias totales\n5. Salir\n-------------------------------')
        opcion = int(input("\nIngrese una opcion: "))
        if opcion==1:
            comprar()
        elif opcion==2:
            mostrar_departamentos()
        elif opcion==3:
            ver_compradores()
        elif opcion==4:
            mostrar_ventas_totales()
        elif opcion==5:
            salir()
        else:
            print("\nIngrese una opcion valida!")

depa_disponibles = [["D"] * 4 for _ in range(10)]

def mostrar_departamentos():
    
    for piso,departamentos in enumerate(depa_disponibles,start=1):
        print(f"\nPiso {piso}:\n",end=" ")
        for i,disponibles in enumerate(departamentos):
            tipo = chr(65 + i)
            if disponibles =="D":
                print(f"{tipo}{piso} []",end=' ')
            if disponibles=="X":
                print(f"{tipo}{piso} [X]",end=' ')
        print()

lista_compradores=[]
depa_compradores=[]

lista_a=[]
lista_b=[]
lista_c=[]
lista_d=[]

def comprar():
    
    while True:
        
        mostrar_departamentos()
        piso = int(input('Ingrese el numero de piso del departamento (de 1 a 10): '))
        if piso in range(1,11):
            tipo = int(input("\nIngrese tipo de departamento a comprar(de 1 a 4):\n\n1. Tipo A     3.800 UF\n2. Tipo B     3.000 UF\n3. Tipo C     2.800 UF\n4. Tipo D     3.500 UF\n"))
            if tipo in range (1,6):
            
                if depa_disponibles[piso-1][tipo-1] != "D":
                    print("No esta disponible!")
                    True
                else:
                    depa_disponibles[piso-1][tipo-1] = "X"
                    precio = compra[tipo]
                    
                    rut_comprador= input("Ingrese su rut (sin puntos ni guion): ")
                    
                    dv = digito_verificador(rut_comprador)
                    rut_validado = rut_comprador+"-"+str(dv)
                    lista_compradores.append(rut_validado)
                    
                    
                    if tipo==1:
                        lista_a.append(1)
                    if tipo==2:
                        lista_b.append(1)
                    if tipo==3:
                        lista_c.append(1)
                    if tipo==4:
                        lista_d.append(1)
                        
                    break
                    
            else:
                print("Ingrese una opcion valida!")
                True
        else:
            print("Ingrese una opcion valida!")
            True
def ver_compradores():
    
    ordenar = sorted(lista_compradores)
    
    for comprador in ordenar:
        print("")
        print(comprador)

def mostrar_ventas_totales():
    
    tipo_a = len(lista_a)
    tipo_b = len(lista_b)
    tipo_c = len(lista_c)
    tipo_d = len(lista_d)
    
    total_a=tipo_a*compra[1]
    total_b=tipo_b*compra[2]
    total_c=tipo_c*compra[3]
    total_d=tipo_d*compra[4]
    
    print("\nTIPO DE DEPARTAMENTO   CANTIDAD     TOTAL\n")
    print(f"Tipo A     3.800 UF     {tipo_a}             {total_a}\nTipo B     3.000 UF     {tipo_b}             {total_b}\nTipo C     2.800 UF     {tipo_c}             {total_c}\nTipo D     3.500 UF     {tipo_d}             {total_d}")
    print(f"\nTOTAL                   {tipo_a+tipo_b+tipo_c+tipo_d}             {total_a+total_b+total_c+total_d}")
import datetime
def salir():
    print("\nHA SALIDO DEL SISTEMA")
    print("JOAQUIN ROMERO")
    fecha = datetime.date.today().strftime('%d/%m/%Y')
    print(fecha)
    exit()
    
menu()      
