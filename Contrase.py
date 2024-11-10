

def contiene_mayusculas(cadena):
    return any(c.isupper() for c in cadena)

def modelos(contraseña):
    caracteres_especiales = "#@/?*&$%^!;:<>=-_+(){}[].,'\" "
    
    if len(contraseña) >= 12 and any(caracter in contraseña for caracter in caracteres_especiales) and contiene_mayusculas(contraseña):
        return "Strong"
    elif len(contraseña) >= 6 and contiene_mayusculas(contraseña):
        return "Moderate"
    else:
        return "Weak"



def Dura(modelo):   
    if modelo == "Strong":
        return True

    if modelo == "Moderate":
        return True

    if modelo == "Weak":
        print("contraseña debil pruebe otra contraseña")
        return False



if __name__ == '__main__':
    #primeraVez = True
    while True:
        contraseña = input("Introduce una contraseña: ")
        if Dura(modelos(contraseña)):
            if modelos(contraseña) == "Strong":
                print("La contraseña {} es fuerte".format(contraseña))

            if modelos(contraseña) == "Moderate":
                print("La contraseña {} es moderada".format(contraseña))
            break
        else:
            continue    



    
    


