import Connector
import petl as etl



databaseSumber = "db_supermarket"
databaseDimensional = "db_dimensional"

def getTableValue(cursorArgs, queryArgs):
    cursorArgs.execute(queryArgs)
    data = cursorArgs
    return data

def tableSourceToDimension(cursorArgs,cursorDm,dbConnection,queryArgs,queryInsert):
    cursorArgs.execute(queryArgs)
    datas = cursorArgs

    for data in datas.fetchall():
        cursorDm.execute(queryInsert%data)
        dbConnection.commit()


def truncateDatabase(dm):
    print("masuk")
    truncate = getTableValue(dm,"SELECT CONCAT('TRUNCATE TABLE ', TABLE_NAME) FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = 'db_dimensional';")
    #print(truncate)
    #dm.execute("SET FOREIGN_KEY_CHECKS=0;")
    print("masuk ke truncate")
    for a in truncate.fetchall():
        dm.execute(a[0])
        print(a[0])


    print("end")


def main():
    dbSource = Connector.sql_connect(databaseSumber)# melakukan koneksi ke database source
    dbSource.autocommit_mode
    ds=dbSource.cursor()# membuat kursor untuk melakukan eksekusi
    dbDimen = Connector.sql_connect(databaseDimensional)
    dm=dbDimen.cursor()
    dm.execute("SET FOREIGN_KEY_CHECKS=0;")
    dbDimen.commit()
    truncateDatabase(dm)
    dbDimen.commit()

    #======================== LIST EXTRACT TRANSFORM DATA ========================#
    qBarang = "SELECT id_barang,tb_kategori_barang.nama_kat_brg,nama_barang " \
              "FROM tb_barang INNER JOIN tb_kategori_barang ON tb_barang.id_kat_brg = tb_kategori_barang.id_kat_brg"

    qCustomer = "SELECT id_member, nama_member, no_telp FROM tb_member"

    qPegawai = "SELECT `tb_pegawai`.`id_pegawai`, `tb_pegawai`.`nama_pegawai`, `tb_role`.`nama_role` FROM `tb_pegawai`" \
               "INNER JOIN `tb_role` ON `tb_role`.`id_role` = `tb_pegawai`.`id_role`"

    qCabang = 'SELECT tb_cabang.`id_cabang`, tb_cabang.`nama_cabang`, CONCAT(tb_cabang.`alamat`,", ",tb_kabupaten.`nama_kabupaten`,", ",tb_provinsi.`nama_provinsi`) AS alamat ' \
              'FROM tb_cabang ' \
              'INNER JOIN tb_kabupaten USING (id_kabupaten) ' \
              'INNER JOIN tb_provinsi USING  (id_provinsi)'

    qInsertBarang = "INSERT INTO tb_dimensi_barang(id_barang,kategori_barang,nama_barang) VALUES('%i','%s','%s');"

    qInsertCustomer = "INSERT INTO tb_dimensi_customer(id_customer,nama_customer,no_telp) VALUES('%i','%s','%s');"

    qInsertPegawai = "INSERT INTO tb_dimensi_pegawai(id_pegawai,nama_pegawai, role) VALUES('%i','%s','%s');"

    qInsertCabang = "INSERT INTO tb_dimensi_cabang(id_cabang,nama_cabang, alamat_kab_prov) VALUES('%i','%s','%s');"

    tableSourceToDimension(ds,dm,dbDimen,qBarang,qInsertBarang)
    tableSourceToDimension(ds,dm,dbDimen,qCustomer,qInsertCustomer)
    tableSourceToDimension(ds,dm,dbDimen,qPegawai,qInsertPegawai)
    tableSourceToDimension(ds,dm,dbDimen,qCabang,qInsertCabang)

    dbDimen.close()
    dbSource.close()

    
if __name__ == "__main__":
    main()

