def promedio(notas):
    return round(sum(notas) / len(notas))


def examen(notas):
    prom = promedio(notas)
    if len(notas) > 2:
        return round((40 - prom * 0.6) / 0.4)
    else:
        return round((40 - prom * 0.5) / 0.5)


def examen_segunda(notas):
    prom = promedio(notas)
    if len(notas) > 2:
        return round((37 - prom * 0.6) / 0.4)
    else:
        return round((37 - prom * 0.5) / 0.5)
