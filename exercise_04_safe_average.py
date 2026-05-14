# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    """
    Lee un archivo donde hay UN número por línea y retorna el promedio de
    los números válidos (como float).

    Reglas:
    - Las líneas que no se puedan convertir a float deben ignorarse (usar
      try/except ValueError internamente).
    - Las líneas vacías también se ignoran.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo existe pero no contiene ningún número válido, lanzar
      ValueError("no valid numbers").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        float - promedio de los números válidos.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si no hay números válidos en el archivo.

    Ejemplo:
        # archivo contiene: "10\n20\nno_es_un_numero\n30\n"
        safe_average("numeros.txt") -> 20.0
    """
    numeros_validos = []
    with open(filename, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            contenido = linea.strip()
            if not contenido:
                continue
            try:
                numero = float(contenido)
                numeros_validos.append(numero)
            except ValueError:
                continue
    if not numeros_validos:
        raise ValueError("no valid numbers")
    total = 0
    for n in numeros_validos:
        total += n

    return total / len(numeros_validos)
