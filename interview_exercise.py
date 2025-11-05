import sqlite3
import pandas as pd

# Loads a CSV in Pandas
df = pd.read_csv('nyc_flights_fixed.csv')

# Creates a SQLite memory DB
conn = sqlite3.connect(':memory:')

# Upload the dataframe as a SQL table
df.to_sql('nyc_flights_fixed', conn, index=False, if_exists='replace')

# Execute SQL query: After each comment, the query for the item will be written.
# Only the query that should be seen has to be called 'query'

###1. Determine the number of distinct destinations connected to the airport.
query = """
SELECT COUNT(DISTINCT dest) distinct_destinations
FROM nyc_flights_fixed
WHERE origin = 'EWR'
"""

###2. Calculate the rounded average of distinct destinations for each day.
query_2 = """
SELECT date, ROUND(AVG(destinations),0) AS rounded_destinations
FROM
  (SELECT date(time_hour) as date, count(distinct dest) destinations
  FROM nyc_flights_fixed
  WHERE origin = 'EWR'
  GROUP BY 1)
"""

###4. Identify the month with the highest number of flights.
query_3 = """
SELECT strftime('%m',date(time_hour)) as date_month, count(*)
FROM nyc_flights_fixed
WHERE origin = 'EWR'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1
"""

resultado = pd.read_sql_query(query, conn)
print(resultado)
#SELECT , COUNT(DISTINCT dest) AS destinations_count
