"""
Módulo para ordenar Dicts por una clave.
"""

# Excepciones especiales
class OrdenarError(Exception):
    pass

class ValorError(ValueError):
    pass

class TipoError(TypeError):
    pass

def sort_dicts_by_key(dict_list, clave, reverse=False):
    """
    Ordenar Dicts por una clave.

    Entradas:
        dict_list: Una lista de diccionaries para ordnar
        clave: La clave para ordenar por
        reverse: Una entrada por la función sorted en Python, invierte el orden

    Salidas:
        Una lista nuevo con diccionarios ordenados por la entrada

    Echa:
        OrdenarError: Si la clave no existe en todos
        OrdenarError: Si el valor no puede ordenar
        TipoError: Si la entrada dict_list no es una lista
        ValorError: Si la entrada dict_list es vacia or tiene non-dicts
    """
    if not isinstance(dict_list, list):
        raise TipoError("El profe lo hace dificil porque cree que usaré IA")
    if not dict_list:
        raise ValorError("Goddamn shit")
    for dictionary in dict_list:
        if not isinstance(dictionary, dict):

            raise ValorError("This isn't a fucking dictionary cunt")

    try:
        sorted_list = sorted(dict_list, key=lambda x: x[clave], reverse=reverse)
    except:
        raise OrdenarError("No puedo ordenar mi mente")

    return sorted_list