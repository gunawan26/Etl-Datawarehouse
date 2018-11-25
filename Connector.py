import pymysql


def sql_connect(dbNameArg):
    try:
        conn = pymysql.connect(user="root", passwd="", host="127.0.0.1", port=3306, database=dbNameArg)

        print("berhasil terkoneksi dengan database "+dbNameArg)

        return conn
        #cur.execute("select * from")
    except:
        print("Failed To connected with the Database.")


