def celkova_cena(pocet_cestujucich, pocet_km):
    if not isinstance(pocet_km, (float, int)):
        raise TypeError('Pocet km musi byt cislo')
    if pocet_km <= 0:
        raise ValueError('Pocet km musi byt kladny')
    km_bus = 0.87
    km_mini = 0.4

    minibus, autobus = pocet_prostriedkov(pocet_cestujucich).values()

    celkova_cena = float((minibus * km_mini * pocet_km) + (autobus * km_bus * pocet_km))
    celkova_cena = round(celkova_cena, 2)
    return f'Cena : {celkova_cena} eur'


def pocet_prostriedkov(pocet_cestujucich):
    minibus = 0
    autobus = 0
    if not isinstance(pocet_cestujucich, (float, int)):
        raise TypeError('Pocet cestujucich musi byt cislo')
    elif pocet_cestujucich <= 0:
        raise ValueError('Pocet cestujucich musi byt kladny')
    while pocet_cestujucich > 0:
        if pocet_cestujucich >= 51:
            autobus += 1
            pocet_cestujucich -= 51
        elif pocet_cestujucich >= 31:
            autobus += 1
            pocet_cestujucich -= 51
        elif pocet_cestujucich >= 15:
            minibus += 1
            pocet_cestujucich -= 15
        else:
            minibus += 1
            pocet_cestujucich -= pocet_cestujucich
    return {'mini': int(minibus), 'bus': int(autobus)}


#print(pocet_prostriedkov(307))
#print(celkova_cena(307, 1))
