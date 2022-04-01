import sqlite3

con = sqlite3.connect("data/movimientos.db")

cur = con.cursor()

cur.execute("""
                select fecha, hora, concepto, es_ingreso, cantidad
                from movimientos
                order by fecha, hora
""")

consulta = cur.fetchall()

print(consulta)
con.close()