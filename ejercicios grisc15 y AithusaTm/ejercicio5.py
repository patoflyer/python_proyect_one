temperaturas = []

for i in range(1, 6):
    print(f"Temperaturas del día {i}:")
    tmax = float(input("Temperatura máxima: "))
    tmin = float(input("Temperatura mínima: "))
    temperaturas.append((tmax, tmin))

temperaturas_medias = []
for tmax, tmin in temperaturas:
    temperatura_media = (tmax + tmin) / 2
    temperaturas_medias.append(temperatura_media)

for i, temperatura_media in enumerate(temperaturas_medias):
    print(f"La temperatura media del día {i+1} fue: {temperatura_media:.2f}")


temperaturas_minimas = [tmin for _, tmin in temperaturas]
minima_temperatura = min(temperaturas_minimas)
dias_con_menos_temperatura = [i+1 for i, tmin in enumerate(temperaturas_minimas) if tmin == minima_temperatura]
print(f"Los días con menos temperatura fueron: {dias_con_menos_temperatura}")

temperatura_busqueda = float(input("Introduce una temperatura máxima a buscar: "))
dias_con_temperatura_busqueda = [i+1 for i, (tmax, _) in enumerate(temperaturas) if tmax == temperatura_busqueda]
if dias_con_temperatura_busqueda:
    print(f"Los días con temperatura máxima {temperatura_busqueda} fueron: {dias_con_temperatura_busqueda}")
else:
    print(f"No se encontraron días con temperatura máxima {temperatura_busqueda}.")
