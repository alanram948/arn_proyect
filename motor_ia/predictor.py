#revision/prediccion provisional 
def predict(cadena):
    longitud = len(cadena)

    if "AUG" in cadena:
        funcion = "codificante"
        prob = 0.85
    elif longitud < 50:
        funcion = "regulatoria"
        prob = 0.70
    else:
        funcion = "desconocida"
        prob = 0.40

    return funcion, prob