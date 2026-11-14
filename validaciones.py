import json
import isalfaperobie
import random

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()

        if valor:
            return valor
        print("  Este campo no puede estar vacío.")
        
def pedir_nom_y_genero(mensaje):
    while True:
        texto = pedir_texto(mensaje)
        if isalfaperobie.es_texto_valido(texto):
            return texto
        print("No puede contener dígitos ni caracteres especiales")


def pedir_email(mensaje):
    while True:
        valor = pedir_texto(mensaje)
        if "@" in valor and "." in valor.split("@")[-1]:
            return valor.lower()
        print("  E-mail no válido.")


def pedir_entero(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("  Escribe un número entero mayor que cero.")


def pedir_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        partes = valor.split("-")
        print(partes, len(partes))
        if (len(partes) == 3 and all(x.isdigit() for x in partes)
                and len(partes[0]) == 2 and len(partes[1]) == 2 and len(partes[2]) == 4
                and 1 <= int(partes[1]) <= 12 and 1 <= int(partes[0]) <= 31):
            return valor
        print("  Formato inválido. Usa DD-MM-AAAA (ej. 06-11-2001).")


def buscar_por_id(lista, identificacion):
    for item in lista:
        if item["Num_Cedula"] == identificacion:
            return item
    return None

def crear_contraseña():
    contraseña = ""
    for i in range(8):
        contraseña += str(random.randint(0,9))
    return contraseña


