# 1. Genere un script que pregunte al usuario por montos de ventas entre un rango de años determinado
# para luego mostrar por pantalla una Serie con los datos de las ventas indexadas por año, tanto antes
# como después de aplicarles un descuento de 10% (ventas con y sin descuento).

import pandas as pd

# anio_cota_baja = int(input("Ingrese el año de cota baja: "))
# anio_cota_alta = int(input("Ingrese el año de cota alta: "))

anio_cota_baja = 2020
anio_cota_alta = 2021

data = {
    'anio': [2020, 2020, 2020, 2020, 2020,
            2021, 2021, 2021, 2021, 2021,
            2022, 2022, 2022, 2022, 2022,
            2023, 2023, 2023, 2023, 2023,
            2024, 2024, 2024, 2024, 2024],
    
    'monto': [1500, 2500, 3000, 4000, 3500,
              4500, 2500, 5500, 6500, 7500,
              9500, 8500, 6500, 7500, 7000,
              5000, 4500, 6000, 8000, 9000,
              11000, 12000, 13000, 14000, 15000],
}

df = pd.DataFrame(data)

df["monto_con_descuento"] = df["monto"]*0.9

print(df)