
import fdb
con=fdb.connect(host='5.179.17.100', database='SLRS_1884_WORK',user='SYSDBA',password='175GPS02')
cur=con.cursor()
cur.execute("select * from Satellites")
for row in cur.fetchall():
    print(row[1],row[2],row[5])
