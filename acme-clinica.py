"""
Guion Login con admin@acmeclinic.com, primero con una contraseña incorrecta y luego con la correcta.
Registrar un médico, cerrar sesión y entrar con ese médico. 
Registrar un paciente y luego intentar registrarlo de nuevo con la misma identificación.
Intentar diagnosticar a un paciente que no está registrado.
Diagnosticar al paciente registrado con 2 síntomas y 2 medicamentos, y mostrar el JSON de la prescripción. 
Cerrar el programa, volver a abrirlo y consultar la historia clínica por identificación (esto comprueba la persistencia).
"""

import json
import carga_y_guarda
import registros

ARCH_USUARIOS = "usuarios.json"
ARCH_PACIENTES = "pacientes.json"
ARCH_CONSULTAS = "consultas.json"
ARCH_MEDICOSCARGA = "reporte_carga_medicos.json"


def login():
    print("=== CLÍNICA ACME - Inicio de sesión ===")
    intentos = 3
    while intentos > 0:
        print(f"\nTienes {intentos} intentos")
        email = input("Usuario (e-mail): ").strip().lower()
        password = input("Contraseña: ")
        intentos -= 1
        for u in carga_y_guarda.cargar(ARCH_USUARIOS):
            if u["email"].lower() == email and u["password"] == password:
                print(f"\nBienvenido, {u['nombres']} {u['apellidos']} ({u['rol']})")
                return u
        print("Credenciales incorrectas.\n")
    print("Demasiados intentos fallidos.")
    return None

def menu(usuario):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar usuario")
        print("2. Registrar paciente")
        print("3. Diagnosticar paciente")
        print("4. Historia clínica")
        print("5. Reporte de medicos")
        print("0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            registros.registrar_usuario(usuario)
        elif opcion == "2":
            registros.registrar_paciente()
        elif opcion == "3":
            registros.diagnosticar(usuario)
        elif opcion == "4":
            registros.historia_clinica()
        elif opcion == "5":
            registros.reporte_medicos(usuario)            
        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida.")
            
            
def main():
    registros.crear_admin_inicial()
    usuario = login()
    if usuario:
        menu(usuario)

if __name__ == "__main__":
    main()
