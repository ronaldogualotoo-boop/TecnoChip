print("#########-TecnoChip-###########")
def generar_factura(nombre_cliente, precio_base, producto):
    iva = precio_base * 0.15
    total = precio_base + iva
    
    print(f"$$$$$$$$$$$$$$$$$$$$$-FACTURA-$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"Factura a nombre de: {nombre_cliente}")
    print(f"Detalle de producto: {producto}")
    print(f"El valor de su consumo es: {precio_base}")
    print(f"EL iva a pagar es de: {iva}")
    print(f"El valor total incluido iva es: {total}")
    print(f"--------------------------------------------------------")

nombre = input("Hola cliente, dime tu nombre: ")
print("Bienvenido a la tienda", nombre)

while True:
    respuesta = input("Desea entrar al catalogo? -si/no-: ")
    
    if respuesta == "si":
        print("Entrando en el catalogo...")
        print("###################################")
        print("############ CATALOGO #############")
        print("###################################")
        print("-----------------------------------")
        print("1. Tarjetas graficas")
        print("2. Memorias RAM")
        print("3. Fuentes de poder")
        print("-----------------------------------")
        print("###################################")
        categoria = input()
        
        if categoria not in ["1", "2", "3"]:
            print("Opcion no valida")
            continue 
            
       
        if categoria == "1":

            print("###################################")
            print("----------Tarjetas Graficas--------")
            
            print("1. NVIDIA GeForce RTX 5090 ....2335")
            print("2. NVIDIA GeForce RTX 5080 ....1223")
            print("3. NVIDIA GeForce RTX 5070 Ti ..889")
            print("-----------------------------------")
            opcion = input()
            if opcion == "1": precio, componente = 2335, "NVIDIA GeForce RTX 5090"
            elif opcion == "2": precio, componente = 1223, "NVIDIA GeForce RTX 5080"
            elif opcion == "3": precio, componente = 889, "NVIDIA GeForce RTX 5070 Ti"
            else: precio = 0

        elif categoria == "2":
            print("###################################")
            print("-----------Memorias RAM------------")
            print("-----------------------------------")
            print("1. Corsair Dominator 64GB ......356")
            print("2. Kingston Fury 32GB ..........225")
            print("3. Corsair Vengeance 16GB ......125")
            print("-----------------------------------")

            opcion = input()
            if opcion == "1": precio, componente = 356, "Corsair Dominator 64GB"
            elif opcion == "2": precio, componente = 225, "Kingston Fury 32GB"
            elif opcion == "3": precio, componente = 125, "Corsair Vengeance 16GB"
            else: precio = 0

        elif categoria == "3":
            print("###################################")
            print("----------Fuentes de poder---------")
            print("-----------------------------------")
            print("1. ASUS ROG Thor 1200W .........452")
            print("2. Corsair RM1000x 1000W .......325")
            print("3. EVGA SuperNOVA 850W .........215")
            print("-----------------------------------")
            opcion = input()
            if opcion == "1": precio, componente = 452, "ASUS ROG Thor 1200W"
            elif opcion == "2": precio, componente = 325, "Corsair RM1000x 1000W"
            elif opcion == "3": precio, componente = 215, "EVGA SuperNOVA 850W"
            else: precio = 0

       
        if precio == 0:
            print("Opcion no valida")
        else:
            generar_factura(nombre, precio, componente)
    else:
        print("Gracias por visitar la tienda mas chevere de quito TecnoChip")
        if respuesta == "no":
            break
