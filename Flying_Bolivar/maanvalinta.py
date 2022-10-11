def db_iso_country_name_by_continent(continent):  # Valitaan country taulusta maan nimi ja iso_country


# koodi maanosan perusteella.
sql = f"SELECT DISTINCT iso_country, name from country where continent = '{continent}'"
query_cursor = connection.cursor()
query_cursor.execute(sql)
result = query_cursor.fetchall()
return result