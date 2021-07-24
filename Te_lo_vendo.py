import random
import time
# : ID, nombre, apellido, edad y contraseña

productos = []
clientes = [{"id": 1, "nombre": "usuario1", "apellido": "Rojas", "contraseña": "123456"},
            {"id": 2, "nombre": "usuario2", "apellido": "Rojas", "contraseña": "123456"},
            {"id": 3, "nombre": "usuario3", "apellido": "Rojas", "contraseña": "123456"},
            {"id": 4, "nombre": "usuario4", "apellido": "Rojas", "contraseña": "123456"},
            {"id": 5, "nombre": "usuario5", "apellido": "Rojas", "contraseña": "123456"},
            {"id": 6, "nombre": "usuario6", "apellido": "Rojas", "contraseña": "123456"}]


def generate_id(lista):
    if(len(lista) == 0):
        return 1    
    return int(lista[-1]['id'])+1

productos_iniciales = ["vasos", "cucharas", "cuchillos", "tenedores"]

for nombre in productos_iniciales:
    producto = {"id": generate_id(productos), "nombre": nombre,"descripcion": f"descripcion de {nombre}", "stock": random.randint(300, 500)}
    productos.append(producto)


def agregar_stock(producto: dict, cantidad: int):
    producto["stock"] += cantidad


def descontar_stock(producto: dict, cantidad: int):
    if producto["stock"] > 0 and producto["stock"] >= cantidad:        
        producto["stock"] -= cantidad
        validar_stock(producto)
    else:
        print("Sin stock suficiente")
    

def mostrar_productos():
    for producto in productos:
        print(
            f"{producto['nombre']} {producto['nombre']} {producto['nombre']}")
        time.sleep(1)


def eliminar_producto(producto_indice):
    productos.pop(producto_indice)


def validar_stock(producto: dict):
    if producto['stock'] < 400:
        print(f"El producto {producto['nombre']}")

def agregar_producto(producto: dict):
    productos.append(producto)
    
def agregar_cliente(cliente:dict):
    clientes.append(cliente)

def eliminar_cliente(cliente_id:int):
    for cliente in clientes:
        if(cliente['id']== cliente_id):
            clientes.remove(cliente)
            return

def mostrar_clientes():
    for cliente in clientes:
        print(cliente)


# El sistema de envío debe ser un programa que pregunta qué tipo de envío es necesario (Rápido
# o largo)
# ● Si es un envío a una distancia de más de 1.000 km es considerado largo. Si es igual o menor a la
# distancia de 1.000 km es considerado rápido.
# ● En el caso que sea un envío rápido debe enviarse a una Bodega_A, caso contrario debe ser
# almacenado a una Bodega_B.
# ● El programa debe verificar que cada bodega no supere las 500 unidades.

bodega_a = []
bodega_b = []

def procesar_envio(distancia):
    if distancia >= 1000:
        envio_largo(distancia)        
    else:
        envio_rapido(distancia)
        
def envio_largo(distancia):
    if(len(bodega_a) < 500):
        bodega_a.append(distancia)
        cuenta = len(bodega_a)
        print(f"{cuenta} - Envio Largo de {distancia}KM a Bodega A")
    else:
        print("Bodega a llena")

def envio_rapido(distancia):
    if(len(bodega_b) < 500):
        bodega_b.append(distancia)
        cuenta = len(bodega_b)
        print(f"{cuenta} - Envio Rapido de {distancia}KM a Bodega B")
    else:
        print("Bodega b llena")

def enviar():
    distancia = input("Ingrese la distancia del envio: ")
    if not distancia.isnumeric():
        print("ingrese una distancia valida")
        enviar()
    else:
        distancia = int(distancia)
        procesar_envio(distancia)
        enviar()
        
enviar()


# while True:
#     procesar_envio(random.randint(999,1001))
#     print(f"A: {len(bodega_a)},B:{len(bodega_b)}")
#     if(len(bodega_a) == 500 and len(bodega_b) ==500 ):
#         break