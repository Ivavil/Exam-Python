from operator import truediv
from random import random

def choose_secret():
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    f = open("palabras_reduced.txt", mode="rt", encoding="utf-8")

    lista_lineas = f.readlines()
    if len(lista_lineas) == 0:
        raise ValueError("EL fichero esta vacio")

    linea = int(random() * len(lista_lineas))
    print(linea)

    for i in range (len(lista_lineas)):
        lista_lineas[i] = lista_lineas[i][:5]

    f.close()

    return (lista_lineas[linea]).upper()
    
def compare_words():
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    if len(word) != len(secret):
        print(len(word))
        print(len(secret))
        print(secret[5])
        raise ValueError("La longitud de las palabras no es la misma")

    same_position = []
    same_letter = []
    for i in range(len(secret) -1):
        if word[i] == secret[i]:
            same_position.append(i)
        else:
            for j in range(len(word)):
                if word[j] == secret[i]:
                    same_letter.append(i)
    return same_position, same_letter

def print_word():
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    if type(same_letter) != list or type(same_position) != list:
        raise ValueError("Los parametros no son listas")

    same_letter_ordered = same_letter.sort()
    same_position_ordered = same_position.sort()

    if same_letter_ordered[0] < 0 or same_letter_ordered[len(same_letter) - 1] > len(same_letter) or same_position_ordered[0] < 0 or same_position_ordered[len(same_position) - 1] > len(same_position):
        raise ValueError("Los valores de los parámetros no son correctos")
    transformed = []
    for i in range(len(word)):
        if same_position.count(i) != 0:
            transformed.append(word[i])
        elif same_letter.count(i) != 0:
            transformed.append(word[i].lower())
            
        else:
            transformed.append("-")

    #for i in range(len(word) - 1):
        #transformed_word = transformed[i] + transformed[i + 1] 
    return transformed[0] + transformed[1] + transformed[2] + transformed[3] + transformed[4]
    
def choose_secret_advanced():
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
    f = open("palabras_extended.txt", mode="rt", encoding="utf-8")

    lista_lineas = f.readlines()
    lista_lineas_menor_5 = filter(lambda s: len(s) == 5, lista_lineas)
    print(lista_lineas_menor_5)

    linea = int(random() * len(lista_lineas_menor_5))
    print(lista_lineas[linea].upper())

    f.close()

    return (lista_lineas[linea]).upper()
 
def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    if selected.count(word) > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    #secret2=choose_secret_advanced()
    secret=choose_secret()
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words()
        resultado=print_word()
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   

    