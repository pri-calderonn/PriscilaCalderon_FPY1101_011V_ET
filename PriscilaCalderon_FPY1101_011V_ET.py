import random




trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
while True:
    print("menu")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5.Salir del programa")

    sueldos=random.randint(300000,2500000)
    cantidad=()
    trabajadores=random.randrange(0,9)
    cantidad=trabajadores*cantidad
    dctosalud=0.7
    dctoAFP=0.12
    liquido=(sueldos)-dctosalud-dctoAFP

    opcion=int(input("Selecciona una opcion 1 - 5 "))
    try:
    
            if opcion ==1:
                print(f"el sueldo de {trabajadores} es $ {sueldos}")
        
            elif opcion==2:

                if sueldos >=800000:
                    print("Clasificar sueldos")
                    print("sueldos menores a 800.000 ")
                    print(f"Total: {cantidad}")
                    print (f"Nombre del empleado: {trabajadores} sueldo : {sueldos}")
                
            
                elif sueldos <=2000000:
                
                    print("Sueldos entre $800.000 y $ 2.000.000")
                    print(f"Total= {cantidad}")
                    print (f"Nombre del empleado: {trabajadores} sueldo : {sueldos}")
                
            
                elif sueldos >2000000:
            
                    print("Sueldos superior a  $ 2.000.000")
                    print(f"Total: {cantidad}")
                    print (f"Nombre del empleado: {trabajadores} sueldo : {sueldos}")
                
                else: 
                    ("opcion invalida")
                
                print(f"Total de sueldos {sueldos}*{cantidad}")
            
            
            
            elif opcion ==3:
                print("Estadisticas")
                print(f"Sueldo mas alto {sueldos}")
                print(f"Sueldo mas bajo {sueldos}")
                print(f"promedio de sueldos")
                print (f"media geometrica")
            
            elif opcion ==4:
                print("Reporte de sueldos")
                print(f"Nombre del empleado: {trabajadores}")
                print(f"Sueldo base: {sueldos}")
                print(f"Descuento de salud: {sueldos-dctosalud}")
                print(f"Descuento de AFP {sueldos - dctoAFP}")
                print(f"Sueldo liquido { liquido}")
            
            elif opcion==5:
                print("Gracias,hasta pronto")
                break
            else: 
                print("opcion no valida ")
            
            
            
            
            
    except ValueError:
        print(f"ingrese opcion valida {opcion}")
        
print("Programa finalizado")
print("Desarrollado por priscila Calderon")
print("Rut: 19.785.815-k")