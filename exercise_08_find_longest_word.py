# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    """
    Lee el archivo, lo divide en palabras (separadas por cualquier tipo
    de whitespace) y retorna la palabra más larga.

    Reglas:
    - Si hay varias palabras con la misma longitud máxima, retornar la
      PRIMERA en aparecer.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo no tiene ninguna palabra (está vacío o solo tiene
      espacios/saltos de línea), lanzar ValueError("file has no words").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        str - la palabra más larga del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si el archivo no tiene palabras.

    Ejemplo:
        # archivo contiene: "el gato corre rapido\npor el jardin\n"
        find_longest_word("texto.txt") -> "rapido"
    """
    palabra_maxima = ""
    encontro_palabras = False

    with open(filename, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        palabras = contenido.split()
        if not palabras:
            raise ValueError("file has no words")
        palabra_maxima = palabras[0]

        for i in range(1, len(palabras)):
            if len(palabras[i]) > len(palabra_maxima):
                palabra_maxima = palabras[i]

    return palabra_maxima
