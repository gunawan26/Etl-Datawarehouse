import Connector
import petl as etl



databaseSumber = "db_supermarket"
databaseDimensional = "db_dimensional"

def getTableValue(cursorArgs, queryArgs):
    cursorArgs.execute(queryArgs)
    data = cursorArgs
    return data

def dataToDimension(curArgs,dataArgs,*args):

    if(range(dataArgs) > 0):
        for row in dataArgs.fetchall():
            print("halo")





def main():
    dbSource = Connector.sql_connect(databaseSumber)# melakukan koneksi ke database source
    ds=dbSource.cursor()# membuat kursor untuk melakukan eksekusi
    dbDimen = Connector.sql_connect(databaseDimensional)
    dm=dbDimen.cursor()
    qBarang = "SELECT id_barang,tb_kategori_barang.nama_kat_brg,nama_barang " \
        "FROM tb_barang INNER JOIN tb_kategori_barang ON tb_barang.id_kat_brg = tb_kategori_barang.id_kat_brg"

    qCabang = "SELECT id_cabang, nama_cabang, alamat, tb_kabupaten.`id_kabupaten` FROM tb_cabang"\
        "INNER JOIN tb_kabupaten ON"\
        "tb_cabang.id_kabupaten = tb_kabupaten.`id_kabupaten`"



    tblMember = getTableValue(ds,qBarang)
    print(tblMember)

    for row in tblMember.fetchall():
        id_barang,kategori_barang,nama_barang = row
        print(id_barang,kategori_barang,nama_barang)
        dm.execute("INSERT INTO tb_dimensi_barang(id_barang,kategori_barang,nama_barang) VALUES('%i','%s','%s');" % (id_barang,kategori_barang,nama_barang))
        dbDimen.commit()#approve insert data.






    dbDimen.close()
    dbSource.close()

    
if __name__ == "__main__":
    main()




    #SELECT tb_barang.id_barang,nama_barang,YEAR(tb_transaksi.`tgl_transaksi`),SUM(tb_detail_transaksi.`harga_satuan`*tb_detail_transaksi.`jmlh_barang`)
    #FROM tb_barang
    #INNER JOIN tb_detail_transaksi ON
    #tb_barang.`id_barang` = tb_detail_transaksi.`id_barang`
    #INNER JOIN tb_transaksi ON
    #tb_detail_transaksi.`id_transaksi` = tb_transaksi.`id_transaksi`
