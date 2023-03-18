#Nombre del archivo: validar.py
#AUTOR: Isaac Ramirez Fernandez
#FECHA: Marzo 18/2023
##DESCRIPCION: Programa que valida nombe, edad y correo
#======================================================
while True:
    menu = """"
    Bienvenidos al registro de usuarios, llene los campos que le soliciten y seleccione un numero del 1 al 3:
    [1]Digitar su Nombre
    [2]Digitar su edad
    [3]Digitar su correo 
    [4]Cerrar Programa
    """

    print(menu)
    opcion = input('Ingrese la opcion 1, 2, 3, 4  ')
#=================Opcion 1 Nombre ==================
    if opcion == "1":
        while True:
            nombre = input('Ingrese su nombre:   ')
            if nombre.isalpha():
                print("Su nombre es:  ", nombre)
                break
            else:
                print("Su nombre esta mal digitado  ")
           
        
#===================Opcion 2 Edad==================        
    elif opcion == "2":
        edad = input("Ingrese su edad  ")
        if edad.isnumeric():
            print("Su edad es de ", edad , "años " )
        else:
            print("Su edad esta digitada de una manera incorrecta")
#=================Opcion 3 Correo =================
    elif opcion == "3":
        correo = input('Ingrese su correo  ')
        if correo.find('@') >=0 and correo.find('.') >=1:
            print("Tu correo es ", correo ) 
        else:
            print('Digitaste erroneamente tu correo')
#===============Opcion 4 Salir =====================
    elif opcion =="4":
        exit()