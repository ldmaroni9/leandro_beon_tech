import sqlite3
import pandas as pd
###1. Determine the number of distinct destinations connected to the airport.
###2. Calculate the rounded average of distinct destinations for each day.
###3. Calculate the average number of destinations per day of the week.
###4. Identify the month with the highest number of flights.


# Cargar CSV en pandas
df = pd.read_csv('nyc_flights_fixed.csv')

# Crear una base de datos SQLite en memoria
conn = sqlite3.connect(':memory:')

# Subir el dataframe como tabla SQL
df.to_sql('nyc_flights_fixed', conn, index=False, if_exists='replace')

# Ejecutar consultas SQL
query = """
SELECT strftime('%m',date(time_hour)) as date_month, count(*)
FROM nyc_flights_fixed
WHERE origin = 'EWR'
GROUP BY 1
ORDER BY 2 DESC

"""
resultado = pd.read_sql_query(query, conn)
print(resultado)
#SELECT , COUNT(DISTINCT dest) AS destinations_count
