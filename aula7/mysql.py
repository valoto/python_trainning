import MySQLdb

con = MySQLdb.connect(
    host="localhost", user="admin", passwd="1234linux", db="escola"
)

cur = con.cursor()


