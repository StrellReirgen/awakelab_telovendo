import time
import os
os.system("cls")
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL =  '\033[91m'
    ENDC =  '\033[0m'
    BOLD =  '\033[1m'
    UNDERLINE = '\033[4m'

bodegas = [{"id": 1, "nombre": "Bodega 1"},
           {"id": 2, "nombre": "Bodega 2"}]

productos = [{"id": 1, "bodega_id": 1, "nombre": "Zapatillas","stock": 20,"unidad":"pares"},
             {"id": 2, "bodega_id": 1, "nombre": "Poleras","stock": 10, "unidad": "pares"},
             {"id": 3, "bodega_id": 1, "nombre": "Zapatos","stock": 15, "unidad": "pares"},
             {"id": 4, "bodega_id": 1, "nombre": "Poleron","stock": 3, "unidad": "pares"},
             {"id": 5, "bodega_id": 1, "nombre": "Chaqueta","stock": 5, "unidad": "pares"},
             {"id": 6, "bodega_id": 1, "nombre": "Guantes", "stock": 4, "unidad": "pares"},
             {"id": 1, "bodega_id": 2, "nombre": "Zapatillas","stock": 100,"unidad":"pares"}]

# Helpers
def generate_id(lista):
    ultimo_id = int(lista[-1]['id'])
    return ultimo_id + 1 if len(lista) > 0 else 1

def obtener_bodega(bodega_id):
    for bodega in bodegas:
        if bodega[id]==bodega_id:
            return bodega
    return {}

# Menu Principal
def menu_principal():
    mostrar_menu_principal()
    opcion = input("Elija una opcion: ")

    if(opcion == '1'):
        agregar_bodega()
    elif(opcion == "2"):
        elegir_bodega()
    elif(opcion == "3"):
        mostrar_stock_tienda()
    elif(opcion == "4"):
        mostrar_stock_tienda_filtrada()
    elif(opcion == '0'):
        print("Hasta luego, vuelve pronto...")
    else:
        print("opcion invalida")
        menu_principal()


def mostrar_menu_principal():
    print(f"{bcolors.OKBLUE} *MENU PRINCIPAL* {bcolors.ENDC}")
    print("1 - Agregar Bodega")
    print("2 - Elegir Bodega")
    print("3 - Mostrar stock productos")
    print("4 - Filtrar stock productos")#pendiente
    print("0 - Salir")

# Opcion 1 - Menu Principal
def agregar_bodega():
    # solicita el nombre y procede a crear la bodega
    while True:
        nombre = input("Ingrese el nombre de la bodega: ")
        if(len(nombre)<6):
            print(f"{bcolors.WARNING}Minimo 6 caracteres {bcolors.ENDC}")
            continue
        break
    id = generate_id(bodegas)
    bodega = { "id" : id, "nombre" : nombre }
    bodegas.append(bodega)
    print(f"{bcolors.OKGREEN}Bodega: {bodega['nombre']} ingresada exitosamente !!{bcolors.ENDC}")
    time.sleep(1)
    menu_principal()

# funcion auxiliar que imprime el listado de bodegas
def mostrar_bodegas():
    for contador,bodega in enumerate(bodegas,start=1):
        print(f"{contador} - {bodega['nombre']}")

# Opcion 2 - Menu Principal
def elegir_bodega():
    mostrar_bodegas()
    print("0 - Volver Menu Principal")
    option = input_elegir_bodega()

    if(option > 0 and option <= len(bodegas) ):
        bodega = bodegas[option-1]
        print(bodega)#testing
        menu_bodega(bodega)
    elif(option == 0):
        menu_principal()
    else:
        print("Opcion Invalida")
        time.sleep(1)
        elegir_bodega()

def input_elegir_bodega():
    opcion = input("Elija una bodega: ")
    if(not opcion.isnumeric()):
        print("Ingrese una opcion valida")
        time.sleep(1.5)
        input_elegir_bodega()
    else:        
        return int(opcion)

# 2.1 Menu Bodega
def menu_bodega(bodega):
    mostrar_menu_bodega(bodega)
    opcion = input("Elija una opcion: ")
    if(opcion == '1'):
        agregar_producto(bodega)
    elif(opcion == '2'):
        actualizar_stock(bodega)
    elif(opcion == "3"):       
        mostrar_productos_bodega(bodega)
    elif(opcion == "4"):
        mostrar_productos_filtrados(bodega)
    elif(opcion == '0'): 
        elegir_bodega()
    else:
        print("opcion incorrecta")
        time.sleep(1)
        menu_bodega(bodega)

# funcion auxiliar para mostrar el menu de la bodega
def mostrar_menu_bodega(bodega):
    print(f"* MENU BODEGA {bodega['nombre']} *")
    print("1 - Agregar producto")
    print("2 - Actualizar stock")
    print("3 - Mostrar stock de productos")
    print("4 - Filtrar stock de productos")
    print("0 - Cambiar de bodega")

# 2.1 Agregar Producto
def agregar_producto(bodega:dict):
    id = generate_id(productos)
    bodega_id = bodega['id']
    nombre = input("Ingrese el nombre: ")
    cantidad = input("Ingrese la cantidad: ")
    unidad = input("Ingrese la unidad: ")
    producto ={"id":id,'bodega_id':bodega_id,'nombre':nombre,'stock':cantidad,'unidad':unidad}
    productos.append(producto)
    print("Producto añadido exitosamente!!")
    time.sleep(1.5)
    menu_bodega(bodega)

# 2.2 Actualizar Stock
def actualizar_stock(bodega):
    productos_bodega = list(obtener_productos_bodega(bodega))
    imprimir_productos_bodega(productos_bodega)
    print("0 - Volver")
    indice_producto = input_elegir_producto()
    if(indice_producto ==0):
        return menu_bodega(bodega)        
    producto = productos_bodega[indice_producto-1]
    nueva_cantidad = input("Ingrese la nueva cantidad: ")
    producto['stock'] = nueva_cantidad
    print(producto)
    time.sleep(1.5)
    menu_bodega(bodega)

def input_elegir_producto():
    producto = input("Elige el producto a modificar: ")
    if not producto.isnumeric():
        print("La opcion tiene que ser un numero")
        time.sleep(1.5)
        input_elegir_bodega()
    else:
        return int(producto)

# funcion auxiliar que devuelve los productos de una bodega concreta
def obtener_productos_bodega(bodega):
    return (producto for producto in productos if producto['bodega_id']==bodega['id'])
    #return filter(lambda producto: producto["bodega_id"] == bodega['id'] , productos)

def imprimir_productos_bodega(productos):
    if len(productos) > 0:
        for indice,producto in enumerate(productos,start=1):
            print(f"{indice} - {producto['nombre']} - {producto['stock']} {producto['unidad']}(s)")
            time.sleep(0.5)
    else:
        print("Sin stock de productos")

# 2.3 Imprime los productos y stock de la bodega
def mostrar_productos_bodega(bodega):
    productos_bodega = list(obtener_productos_bodega(bodega))
    imprimir_productos_bodega(productos_bodega)  
    time.sleep(1.5)
    menu_bodega(bodega)

# 2.4 Imprime un filtro de los productos filtrados
def mostrar_productos_filtrados(bodega):
    productos_bodega = obtener_productos_bodega(bodega)
    cantidad = input_productos_filtrados()
    productos_filtrados = filter(lambda producto: producto["stock"] >= cantidad , productos_bodega)        
    imprimir_productos_bodega(productos_filtrados)
    time.sleep(1.5)
    menu_bodega(bodega)

def input_productos_filtrados():
    cantidad = input("Ingrese la cantidad minima:")    
    if(len(cantidad) == 0 or not cantidad.isnumeric()):
        print(f"{bcolors.WARNING}Ingrese una cantidad{bcolors.ENDC}")
        time.sleep(1)
        input_productos_filtrados()
    else:
        return int(cantidad)

# 3.1 Muestra el stock del stock de todas las
def mostrar_stock_tienda():
    obtener_stock_tienda()
    time.sleep(1)    
    menu_principal()

# 3.2 Muestra stock tienda deacuerdo a un valor minimo
def mostrar_stock_tienda_filtrada():   
    cantidad =  input_stock_tienda_filtrada()
    obtener_stock_tienda(cantidad)
    time.sleep(1.5)
    menu_principal()

def input_stock_tienda_filtrada():
    #solicitamos la cantidad 
    cantidad = input("Ingrese la cantidad minima:")    
    if(len(cantidad) == 0 or not cantidad.isnumeric()):
        print(f"{bcolors.WARNING}Ingrese una cantidad{bcolors.ENDC}")
        time.sleep(1)
        input_stock_tienda_filtrada()
    else:
        #devolvemos la cantidad como entero
        return int(cantidad)

def obtener_stock_tienda(cantidad=0): 
    #funcion que muestra el stock de productos      
    # creamos una seleccion con el nombre de todos los productos
    nombre_productos = set(producto['nombre'] for producto in productos) 
    #recorremos todos los nombres de los productos de la tienda acompañado de un contador   
    for contador,nombre_producto in enumerate(nombre_productos,start=1):
        #sacamos la suma del stock de todos los producto que coincidan con el nombre de la seleccion
        cantidad_total = sum(producto['stock'] for producto in productos if producto['nombre'] == nombre_producto)
        # mostramos solos los producto que superen una cantidad establecida. valor por defecto 0
        if(cantidad_total >= cantidad):
            print(f"{contador} - {nombre_producto} - {cantidad_total}")
        

def telovendo():
    menu_principal()

telovendo()
