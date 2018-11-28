def promedio(notas):
    return round(sum(notas) / len(notas))


def examen(notas):
    prom = promedio(notas)
    if len(notas) > 2:
        return round((39.5 - prom * 0.6) / 0.4)
    else:
        return round((39.5 - prom * 0.5) / 0.5)


def examen_segunda(notas):
    prom = promedio(notas)
    if len(notas) > 2:
        return round((36.5 - prom * 0.6) / 0.4)
    else:
        return round((36.5 - prom * 0.5) / 0.5)
