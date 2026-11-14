def es_texto_valido(texto):
    for caracter in texto:
        if not (caracter.isalpha() or caracter.isspace()):
            return False
    return True
