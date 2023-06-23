def esta_vazio(value):
    ATRIBUTO_INVALIDO = True

    if len(value) != 0:
        for caractere in value:
            if caractere != " ":
                ATRIBUTO_INVALIDO = False
        if ATRIBUTO_INVALIDO:
            return ATRIBUTO_INVALIDO
        else:
            return False
    else:
        return ATRIBUTO_INVALIDO
    