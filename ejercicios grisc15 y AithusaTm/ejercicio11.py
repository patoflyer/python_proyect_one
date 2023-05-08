elementos = {
    "H": {"nombre": "Hidrógeno", "numero_atomico": 1},
    "He": {"nombre": "Helio", "numero_atomico": 2},
    "Li": {"nombre": "Litio", "numero_atomico": 3},
    "Be": {"nombre": "Berilio", "numero_atomico": 4},
    "B": {"nombre": "Boro", "numero_atomico": 5},
    "C": {"nombre": "Carbono", "numero_atomico": 6},
    "N": {"nombre": "Nitrógeno", "numero_atomico": 7},
    "O": {"nombre": "Oxígeno", "numero_atomico": 8},
    "F": {"nombre": "Flúor", "numero_atomico": 9},
    "Ne": {"nombre": "Neón", "numero_atomico": 10},
    "Na": {"nombre": "Sodio", "numero_atomico": 11},
    "Mg": {"nombre": "Magnesio", "numero_atomico": 12}
}

elementos_tuplas = [(elementos[sigla]["numero_atomico"], sigla) for sigla in elementos]

print(elementos_tuplas)
