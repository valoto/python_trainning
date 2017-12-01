import psycopg2

#nome = "Igor Valoto"
#email = "igor@valoto.com.br"

con = psycopg2.connect("host=localhost dbname=loja user=admin password=4linux")

cur = con.cursor()

cur.execute("INSERT INTO alunos (nome, email) VALUES ('Igor Valoto', 'igor@valoto.com.br')")
cur.execute("INSERT INTO alunos (nome, email) VALUES ('Trend Micro', 'trendbr@trendmicro.com')")

cur.execute("DELETE FROM alunos WHERE email='igor@valoto.com.br'")

cur.execute("UPDATE alunos SET email='mudou@trendmicro.com' WHERE email='trendbr@trendmicro.com'")

#con.commit()
#con.close()
