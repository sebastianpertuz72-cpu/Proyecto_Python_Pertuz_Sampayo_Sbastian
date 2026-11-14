import json

def cargar(nombre_archivo):
    try:
        with open(nombre_archivo,"r",encoding="utf-8") as carga:
            return json.load(carga)
    except (FileNotFoundError):
        return []
    
def guardar(nombre_archivo,nuevo_dato):
    with open(nombre_archivo,"w", encoding="utf-8") as guardado:
        json.dump(nuevo_dato,guardado,ensure_ascii=False , indent=4)
            