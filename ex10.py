def invertir_texto(texto):
    resultado = ""
    for letra in texto:
        resultado = letra + resultado
    return resultado

print(invertir_texto("Hola"))